from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    print("ERROR: API key not found")
else:
    print("API key loaded!")

client = Groq(api_key=api_key)

print("Sending message to AI...")

response = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[
        {"role": "user", "content": "You are a GATE exam coach. A student studied Logic Gates today. Give one motivating sentence."}
    ]
)

print("AI says:")
print(response.choices[0].message.content)
print("Phase 2 Complete!")