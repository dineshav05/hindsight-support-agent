from fastapi import FastAPI
from pydantic import BaseModel
import requests
from groq import Groq
from fastapi.middleware.cors import CORSMiddleware

# Initialize Server and Clients
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

HINDSIGHT_API_KEY = "hsk_fa2cc57f9fbb116b235bfeb15af96b5c_bde7a5e63a266d9c"
groq_client = Groq(api_key="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")

class ChatRequest(BaseModel):
    user_id: str
    message: str

class ChatResponse(BaseModel):
    reply: str
    memory_used: list

@app.post("/chat", response_model=ChatResponse)
async def process_chat(request: ChatRequest):
    headers = {
        "Authorization": f"Bearer {HINDSIGHT_API_KEY}",
        "Content-Type": "application/json"
    }
    
    # 1. RECALL: Fetch Sarah's history via Hindsight REST API
    recall_url = f"https://api.hindsight.vectorize.io/v1/default/banks/{request.user_id}/memories/recall"
    recall_payload = {"query": "User environment and previous troubleshooting steps"}
    
    past_context = []
    try:
        recall_res = requests.post(recall_url, headers=headers, json=recall_payload)
        print(f"HINDSIGHT STATUS: {recall_res.status_code}") # Add this line
        print(f"HINDSIGHT DATA: {recall_res.text}") # Add this line
        if recall_res.status_code == 200:
            results = recall_res.json()
            # Extract just the text content from the returned memory items
            past_context = [item.get("text", "") for item in results.get("results", [])]
    except Exception as e:
        past_context = [f"Memory retrieval failed: {str(e)}"]
    
    # 2. THINK: Construct the prompt
    context_string = " | ".join(past_context)
    system_prompt = f"""You are a helpful tech support agent for a B2B software company. 
    Here is the verified past context and environment setup for this user: {context_string}. 
    Do NOT ask the user for information you already know from this context. 
    Skip troubleshooting steps they have already tried."""

    # 3. GENERATE: Send to Groq LLM
    chat_completion = groq_client.chat.completions.create(
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": request.message}
        ],
        model="qwen/qwen3.8-27b",
    )
    llm_reply = chat_completion.choices[0].message.content

    # 4. REMEMBER: Save this new interaction via Hindsight REST API
    retain_url = f"https://api.hindsight.vectorize.io/v1/default/banks/{request.user_id}/memories"
    retain_payload = {
        "items": [{
            "content": f"User asked: {request.message} | Agent replied: {llm_reply}",
            "context": "Ongoing troubleshooting session"
        }]
    }
    requests.post(retain_url, headers=headers, json=retain_payload)
    
    # 5. RESPOND
    return ChatResponse(
        reply=llm_reply, 
        memory_used=past_context
    )