
import os
import requests

from dotenv import load_dotenv

# Load .env from the project root
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
load_dotenv(os.path.join(BASE_DIR, ".env"))

HINDSIGHT_API_KEY = os.getenv("HINDSIGHT_API_KEY")

if not HINDSIGHT_API_KEY:
    raise RuntimeError("HINDSIGHT_API_KEY is missing from .env")

BANK_ID = "sarah_eng_01"

URL = (
    f"https://api.hindsight.vectorize.io/"
    f"v1/default/banks/{BANK_ID}/memories"
)

headers = {
    "Authorization": f"Bearer {HINDSIGHT_API_KEY}",
    "Content-Type": "application/json"
}

payload = {
    "items": [
        {
            "content": "Customer is a Lead Engineer using a Node.js backend hosted on AWS infrastructure.",
            "context": "User environment profiling",
            "timestamp": "2026-11-04T10:00:00Z"
        },
        {
            "content": "Customer reported payment webhook is continually timing out.",
            "context": "Support Ticket #88492 - Webhook Timeout",
            "timestamp": "2026-11-05T14:30:00Z"
        },
        {
            "content": "Guided customer to clear AWS firewall rules and perform a hard reset on all production API keys. Customer confirmed these steps were completed successfully, but the timeout issue persists.",
            "context": "Support Ticket #88492 - Troubleshooting Steps Applied",
            "timestamp": "2026-11-05T15:15:00Z"
        }
    ]
}

print("Pushing historical data to Hindsight...")

try:
    response = requests.post(
        URL,
        headers=headers,
        json=payload,
        timeout=30
    )

    if response.status_code in [200, 201]:
        print("Success! Historical customer data saved.")
    else:
        print(f"Failed. Status code: {response.status_code}")
        print("Response:", response.text[:500])

except requests.RequestException as error:
    print("Hindsight connection failed:", error)
