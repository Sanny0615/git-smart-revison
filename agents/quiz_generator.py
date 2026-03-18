from groq import Groq
import os
import json
from dotenv import load_dotenv

load_dotenv()

SCHEDULE_FILE = "database/schedule.json"

def load_schedule():
    if not os.path.exists(SCHEDULE_FILE):
        return {}
    with open(SCHEDULE_FILE, "r") as f:
        return json.load(f)

def build_database():
    from agents.rag_setup import get_collection
    return get_collection()

def generate_quiz(topic, subject, level, collection):
    results = collection.query(
        query_texts=[f"{topic} {subject} GATE questions"],
        n_results=5
    )

    context = ""
    for i, doc in enumerate(results["documents"][0]):
        source = results["metadatas"][0][i]["source"]
        context += f"[From {source}]:\n{doc}\n\n"

    if level == 1:
        level_instruction = "Generate 7 BASIC theory MCQ questions testing fundamental understanding."
    elif level == 2:
        level_instruction = "Generate 7 APPLIED conceptual MCQ questions testing application."
    else:
        level_instruction = "Generate 7 EXAM-LEVEL MCQ questions similar to actual GATE exam."

    client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    chat = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": f"""You are a GATE exam question generator.
{level_instruction}

Use EXACTLY this format for each question:

Q1: [question]
A) [option]
B) [option]
C) [option]
D) [option]
Answer: [letter only, e.g. A]
Explanation: [one line]

Q2: [question]
A) [option]
B) [option]
C) [option]
D) [option]
Answer: [letter only]
Explanation: [one line]

Continue same format up to Q7. Always put each part on its own line."""},
            {"role": "user", "content": f"Topic: {topic}\nSubject: {subject}\n\nReference material:\n{context}\n\nGenerate 7 questions now."}
        ]
    )

    return chat.choices[0].message.content