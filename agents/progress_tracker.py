import json
import os
from datetime import datetime, timedelta

SCHEDULE_FILE = "database/schedule.json"
PROGRESS_FILE = "database/progress.json"
HISTORY_FILE = "database/session_history.json"
USER_FILE = "database/user.json"

def load_schedule():
    if not os.path.exists(SCHEDULE_FILE):
        return {}
    with open(SCHEDULE_FILE, "r") as f:
        return json.load(f)

def load_progress():
    if not os.path.exists(PROGRESS_FILE):
        return {
            "streak": 0,
            "last_active": None,
            "total_sessions": 0,
            "daily_activity": {}
        }
    with open(PROGRESS_FILE, "r") as f:
        return json.load(f)

def save_progress(progress):
    os.makedirs("database", exist_ok=True)
    with open(PROGRESS_FILE, "w") as f:
        json.dump(progress, f, indent=2)

def load_history():
    if not os.path.exists(HISTORY_FILE):
        return []
    with open(HISTORY_FILE, "r") as f:
        return json.load(f)

def save_history(history):
    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=2)

def load_user():
    if not os.path.exists(USER_FILE):
        return {"name": "Student", "exam": "GATE", "branch": "Computer Science"}
    with open(USER_FILE, "r") as f:
        return json.load(f)

def save_session(topic, subject, level, score, total):
    history = load_history()
    today = datetime.now().strftime("%Y-%m-%d")
    retention = round((score/total) * 100)

    session = {
        "date": today,
        "topic": topic,
        "subject": subject,
        "level": level,
        "score": score,
        "total": total,
        "retention": retention,
        "time": datetime.now().strftime("%H:%M")
    }

    history.append(session)
    save_history(history)

    progress = load_progress()
    progress["total_sessions"] += 1

    if today not in progress["daily_activity"]:
        progress["daily_activity"][today] = 0
    progress["daily_activity"][today] += 1

    last = progress.get("last_active")
    yesterday = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")

    if last == today:
        pass
    elif last == yesterday:
        progress["streak"] += 1
    else:
        progress["streak"] = 1

    progress["last_active"] = today
    save_progress(progress)

    print(f"Session saved! Retention: {retention}%")

def calculate_retention(topic):
    history = load_history()
    topic_sessions = [s for s in history if s["topic"] == topic]

    if not topic_sessions:
        return 0

    recent = topic_sessions[-3:]
    avg = sum(s["retention"] for s in recent) / len(recent)
    return round(avg)

def calculate_overall_retention():
    history = load_history()
    if not history:
        return 0
    recent = history[-10:]
    avg = sum(s["retention"] for s in recent) / len(recent)
    return round(avg)

def check_decay():
    schedule = load_schedule()
    today = datetime.now().strftime("%Y-%m-%d")
    today_date = datetime.now()

    decaying = []
    healthy = []
    completed = []

    for topic, data in schedule.items():
        if data["status"] != "active":
            completed.append(topic)
            continue

        upcoming_dates = [d for d in data["quiz_dates"]
                         if d not in data["completed_sessions"]]

        if not upcoming_dates:
            completed.append(topic)
            continue

        next_date = datetime.strptime(upcoming_dates[0], "%Y-%m-%d")
        days_overdue = (today_date - next_date).days

        if days_overdue >= 0:
            decaying.append({
                "topic": topic,
                "days_overdue": days_overdue,
                "next_quiz": upcoming_dates[0]
            })
        else:
            days_until = abs(days_overdue)
            healthy.append({
                "topic": topic,
                "days_until": days_until,
                "next_quiz": upcoming_dates[0]
            })

    return decaying, healthy, completed

def show_dashboard():
    user = load_user()
    progress = load_progress()
    hour = datetime.now().hour

    if hour < 12:
        greeting = "Good morning"
    elif hour < 17:
        greeting = "Good afternoon"
    else:
        greeting = "Good evening"

    print("\n" + "="*50)
    print(f"  {greeting}, {user['name']}!")
    print(f"  {user['exam']} • {user['branch']}")
    print("="*50)

    streak = progress["streak"]
    total = progress["total_sessions"]
    retention = calculate_overall_retention()

    print(f"\n🔥 Study Streak: {streak} days")
    print(f"📚 Total Sessions: {total}")
    print(f"🧠 Overall Retention: {retention}%")

    decaying, healthy, completed = check_decay()

    print(f"\n{'='*50}")
    print("📊 TOPIC HEALTH")
    print(f"{'='*50}")

    if decaying:
        print(f"\n⚠️  NEEDS ATTENTION ({len(decaying)}):")
        for t in decaying:
            ret = calculate_retention(t["topic"])
            if t["days_overdue"] > 2:
                print(f"   🔴 {t['topic']} — {t['days_overdue']} days overdue! Retention: {ret}%")
            else:
                print(f"   🟡 {t['topic']} — due today! Retention: {ret}%")

    if healthy:
        print(f"\n✅ HEALTHY ({len(healthy)}):")
        for t in healthy:
            ret = calculate_retention(t["topic"])
            print(f"   🟢 {t['topic']} — next in {t['days_until']} days. Retention: {ret}%")

    if completed:
        print(f"\n🏆 GRADUATED ({len(completed)}):")
        for t in completed:
            print(f"   ⭐ {t}")

    print(f"\n{'='*50}")
    print("📅 ACTIVITY WALL (Last 7 days)")
    print(f"{'='*50}\n")

    activity = progress.get("daily_activity", {})
    for i in range(6, -1, -1):
        day = (datetime.now() - timedelta(days=i)).strftime("%Y-%m-%d")
        day_short = (datetime.now() - timedelta(days=i)).strftime("%a %d")
        sessions = activity.get(day, 0)
        bar = "🟩" * min(sessions, 5) if sessions > 0 else "⬜"
        print(f"  {day_short}: {bar} {sessions} sessions")

    print()

def show_history():
    history = load_history()
    if not history:
        print("\nNo sessions completed yet!")
        return

    print("\n" + "="*50)
    print("  SESSION HISTORY")
    print("="*50)

    for session in reversed(history[-10:]):
        print(f"\n📅 {session['date']} {session['time']}")
        print(f"   Topic: {session['topic']}")
        print(f"   Subject: {session['subject']}")
        print(f"   Level: {session['level']}/3")
        print(f"   Score: {session['score']}/{session['total']}")
        print(f"   Retention: {session['retention']}%")

if __name__ == "__main__":
    print("================================")
    print("   PROGRESS TRACKER AGENT      ")
    print("================================")

    print("\nWhat do you want to do?")
    print("1. View Dashboard")
    print("2. View Session History")
    print("3. Test Save Session")
    print()

    choice = input("Choose (1/2/3): ")

    if choice == "1":
        show_dashboard()
    elif choice == "2":
        show_history()
    elif choice == "3":
        save_session("OS", "Operating Systems", 1, 2, 3)
        print("Test session saved!")