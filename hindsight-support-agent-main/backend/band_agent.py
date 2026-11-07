import os
import asyncio
import traceback
from pathlib import Path

import requests
from dotenv import load_dotenv
from band import Agent
from band.core import SimpleAdapter


# --------------------------------------------------
# LOAD ENVIRONMENT VARIABLES
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

BAND_AGENT_ID = os.getenv("BAND_AGENT_ID")
BAND_API_KEY = os.getenv("BAND_API_KEY")

SUPPORT_API_URL = os.getenv(
    "SUPPORT_API_URL",
    "http://127.0.0.1:8000/chat"
)


# --------------------------------------------------
# BAND MESSAGE ADAPTER
# --------------------------------------------------

class SupportAdapter(SimpleAdapter):

    async def on_message(
        self,
        msg,
        tools,
        history,
        participants_msg,
        contacts_msg,
        *,
        is_session_bootstrap,
        room_id
    ):

        user_message = (msg.content or "").strip()

        print("DEBUG sender_type:", repr(msg.sender_type))
        print("DEBUG sender_id:", repr(msg.sender_id))

        # Ignore messages that are not from users
        if str(msg.sender_type).lower() != "user":
            await tools.no_reply("Ignoring non-user message")
            return

        # Ignore empty messages
        if not user_message:
            await tools.no_reply("Empty message")
            return

        print(f"\nBAND message received: {user_message}")

        try:

            # Use the BAND sender ID as the Hindsight user ID
            band_user_id = str(msg.sender_id)

            # Forward the message to the FastAPI backend
            response = await asyncio.to_thread(
                requests.post,
                SUPPORT_API_URL,
                json={
                    "user_id": band_user_id,
                    "message": user_message
                },
                timeout=60
            )

            response.raise_for_status()

            data = response.json()
            reply = data.get("reply")

            if not isinstance(reply, str) or not reply.strip():
                raise ValueError("Backend returned an empty reply")

            print("Backend reply received. Sending to BAND...")

            # Send reply with the required participant mention
            await asyncio.wait_for(
                tools.send_message(
                    reply,
                    mentions=["yashasdsalanke"]
                ),
                timeout=15
            )

            print("BAND reply sent successfully.")

        except Exception as error:
            print("BAND HANDLER ERROR:", repr(error))
            traceback.print_exc()


# --------------------------------------------------
# START BAND AGENT
# --------------------------------------------------

async def main():

    if not BAND_AGENT_ID or not BAND_API_KEY:
        raise RuntimeError(
            "BAND_AGENT_ID or BAND_API_KEY is missing from .env"
        )

    agent = Agent.create(
        adapter=SupportAdapter(),
        agent_id=BAND_AGENT_ID,
        api_key=BAND_API_KEY
    )

    try:

        await agent.start()

        print("\n================================")
        print("BAND SUPPORT AGENT IS RUNNING")
        print("Waiting for customer messages...")
        print("================================\n")

        await agent.run_forever()

    finally:
        await agent.stop()


# --------------------------------------------------
# RUN APPLICATION
# --------------------------------------------------

if __name__ == "__main__":
    asyncio.run(main())