import requests

HINDSIGHT_API_KEY = "hsk_fa2cc57f9fbb116b235bfeb15af96b5c_bde7a5e63a266d9c"
BANK_ID = "sarah_eng_01"
# The exact REST URL for retaining memories
URL = f"https://api.hindsight.vectorize.io/v1/default/banks/{BANK_ID}/memories"

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

print("Pushing historical data to Hindsight via REST API...")
response = requests.post(URL, headers=headers, json=payload)

if response.status_code in [200, 201]:
    print("Success! Sarah's past interactions are now locked in memory.")
else:
    print(f"Failed to push data. Status Code: {response.status_code}")
    print(response.text)