from groq import Groq

client = Groq(api_key="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")

print("Active models available to your API key:")
# This fetches the live list of models your specific account has access to
models = client.models.list()
for m in models.data:
    print(f"- {m.id}")