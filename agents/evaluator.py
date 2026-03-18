from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

groq_client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def evaluate_mcq(student_answer, correct_answer, question, explanation):
    is_correct = student_answer.strip().upper() == correct_answer.strip().upper()
    
    if is_correct:
        feedback = f"Correct! {explanation}"
        verdict = "CORRECT"
    else:
        feedback = f"Not quite! The correct answer is {correct_answer}. {explanation}"
        verdict = "INCORRECT"
    
    return {
        "verdict": verdict,
        "feedback": feedback,
        "score": 1 if is_correct else 0
    }

def evaluate_theory(question, student_answer, topic, subject):
    response = groq_client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": """You are a GATE exam evaluator.
Evaluate the student answer on 3 things:
1. CORE CONCEPT: Is the main idea correct? (Yes/No)
2. ACCURACY: Are technical terms used correctly? (Score 0-2)
3. COMPLETENESS: Are main points covered? (Score 0-2)

Then give:
VERDICT: STRONG / PARTIAL / WEAK
SCORE: total out of 4
FEEDBACK: One encouraging sentence
HINT: One guiding question to improve (never give away answer directly)

Format exactly like:
VERDICT: [STRONG/PARTIAL/WEAK]
SCORE: [0-4]/4
FEEDBACK: [one sentence]
HINT: [one guiding question]"""},
            {"role": "user", "content": f"""Topic: {topic}
Subject: {subject}
Question: {question}
Student Answer: {student_answer}

Evaluate this answer."""}
        ]
    )
    
    result = response.choices[0].message.content
    
    lines = result.strip().split("\n")
    verdict = "PARTIAL"
    score = 2
    feedback = ""
    hint = ""
    
    for line in lines:
        if line.startswith("VERDICT:"):
            verdict = line.replace("VERDICT:", "").strip()
        elif line.startswith("SCORE:"):
            try:
                score = int(line.replace("SCORE:", "").split("/")[0].strip())
            except:
                score = 2
        elif line.startswith("FEEDBACK:"):
            feedback = line.replace("FEEDBACK:", "").strip()
        elif line.startswith("HINT:"):
            hint = line.replace("HINT:", "").strip()
    
    return {
        "verdict": verdict,
        "score": score,
        "feedback": feedback,
        "hint": hint
    }

def run_evaluation_demo():
    print("================================")
    print("   ANSWER EVALUATOR AGENT      ")
    print("================================")
    print()
    
    print("Choose question type:")
    print("1. MCQ Question")
    print("2. Theory Question")
    print()
    choice = input("Choose (1/2): ")
    
    if choice == "1":
        print("\nSample MCQ:")
        question = "Which scheduling algorithm gives minimum average waiting time?"
        print(f"Q: {question}")
        print("A) FCFS")
        print("B) SJF")
        print("C) Round Robin")
        print("D) Priority")
        print()
        
        student_answer = input("Your answer (A/B/C/D): ")
        
        result = evaluate_mcq(
            student_answer=student_answer,
            correct_answer="B",
            question=question,
            explanation="Shortest Job First (SJF) minimizes average waiting time by always executing the shortest job next."
        )
        
        print(f"\nVerdict: {result['verdict']}")
        print(f"Feedback: {result['feedback']}")
    
    elif choice == "2":
        print("\nSample Theory Question:")
        question = "Explain what deadlock is and name its four necessary conditions."
        print(f"Q: {question}")
        print()
        
        student_answer = input("Your answer: ")
        
        print("\nEvaluating your answer...")
        result = evaluate_theory(
            question=question,
            student_answer=student_answer,
            topic="Deadlock",
            subject="Operating Systems"
        )
        
        print(f"\nVerdict: {result['verdict']}")
        print(f"Score: {result['score']}/4")
        print(f"Feedback: {result['feedback']}")
        if result['hint']:
            print(f"Think about: {result['hint']}")

if __name__ == "__main__":
    run_evaluation_demo()