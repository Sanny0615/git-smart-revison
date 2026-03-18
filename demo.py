from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

print("================================")
print("  SMART REVISION SYSTEM - DEMO  ")
print("================================")
print()

while True:
    topic = input("What did you study today? (or type 'exit'): ")
    
    if topic == "exit":
        print("Great work today! See you tomorrow!")
        break
    
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": f"You are a GATE exam coach. A student just studied '{topic}'. Give 3 things: 1) One motivating sentence 2) One key point to remember 3) One tip for GATE exam. Keep it short and energetic!"}
        ]
    )
    
    print()
    print("🤖 Your AI Coach says:")
    print("----------------------")
    print(response.choices[0].message.content)
    print()