import json
import os
from datetime import datetime, timedelta

SCHEDULE_FILE = "database/schedule.json"

EBBINGHAUS_INTERVALS = [1, 3, 7, 14, 21, 30, 60]

def load_schedule():
    if not os.path.exists(SCHEDULE_FILE):
        return {}
    with open(SCHEDULE_FILE, "r") as f:
        return json.load(f)

def save_schedule(schedule):
    os.makedirs("database", exist_ok=True)
    with open(SCHEDULE_FILE, "w") as f:
        json.dump(schedule, f, indent=2)

def add_topic(topic, subject="General"):
    schedule = load_schedule()
    today = datetime.now().strftime("%Y-%m-%d")

    if topic in schedule:
        print(f"Topic '{topic}' already exists!")
        return

    quiz_dates = []
    for interval in EBBINGHAUS_INTERVALS:
        quiz_date = datetime.now() + timedelta(days=interval)
        quiz_dates.append(quiz_date.strftime("%Y-%m-%d"))

    schedule[topic] = {
        "subject": subject,
        "date_added": today,
        "quiz_dates": quiz_dates,
        "completed_sessions": [],
        "current_level": 1,
        "status": "active"
    }

    save_schedule(schedule)
    print(f"Topic '{topic}' added successfully!")
    print(f"Quiz schedule:")
    for i, date in enumerate(quiz_dates):
        print(f"  Day {EBBINGHAUS_INTERVALS[i]:2d} → {date}")

def get_todays_topics():
    schedule = load_schedule()
    today = datetime.now().strftime("%Y-%m-%d")
    due_topics = []

    for topic, data in schedule.items():
        if data["status"] == "active":
            for quiz_date in data["quiz_dates"]:
                if quiz_date == today and quiz_date not in data["completed_sessions"]:
                    due_topics.append({
                        "topic": topic,
                        "subject": data["subject"],
                        "level": data["current_level"],
                        "due_date": quiz_date
                    })
                    break

    return due_topics

def complete_session(topic, quiz_date):
    schedule = load_schedule()
    if topic in schedule:
        schedule[topic]["completed_sessions"].append(quiz_date)
        current_level = schedule[topic]["current_level"]
        if current_level < 3:
            schedule[topic]["current_level"] = current_level + 1
        save_schedule(schedule)
        print(f"Session completed for '{topic}'!")

def show_all_topics():
    schedule = load_schedule()
    if not schedule:
        print("No topics added yet!")
        return

    print("\n=== YOUR REVISION SCHEDULE ===")
    today = datetime.now().strftime("%Y-%m-%d")

    for topic, data in schedule.items():
        print(f"\nTopic: {topic}")
        print(f"Subject: {data['subject']}")
        print(f"Level: {data['current_level']}/3")
        print(f"Status: {data['status']}")

        upcoming = [d for d in data["quiz_dates"] if d >= today]
        if upcoming:
            print(f"Next quiz: {upcoming[0]}")
        else:
            print("All sessions completed!")

if __name__ == "__main__":
    print("================================")
    print("  EBBINGHAUS SCHEDULER AGENT   ")
    print("================================")
    print()

    while True:
        print("1. Add new topic")
        print("2. See today's quizzes")
        print("3. See all topics")
        print("4. Exit")
        print()
        choice = input("Choose (1/2/3/4): ")

        if choice == "1":
            topic = input("What topic did you study? ")
            subject = input("Which subject? (e.g. Digital Logic, OS, DBMS): ")
            add_topic(topic, subject)

        elif choice == "2":
            due = get_todays_topics()
            if due:
                print(f"\nYou have {len(due)} quiz(es) due today!")
                for t in due:
                    print(f"  - {t['topic']} (Level {t['level']})")
            else:
                print("\nNo quizzes due today!")

        elif choice == "3":
            show_all_topics()

        elif choice == "4":
            print("Goodbye!")
            break

        print()