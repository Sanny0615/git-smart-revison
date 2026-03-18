import streamlit as st
from datetime import datetime, timedelta
from agents.progress_tracker import (
    load_user, load_progress, calculate_overall_retention,
    calculate_retention, check_decay
)


def greet():
    h = datetime.now().hour
    if h < 12:
        return "Good morning"
    elif h < 17:
        return "Good afternoon"
    return "Good evening"


def show():
    user = load_user()
    progress = load_progress()
    retention = calculate_overall_retention()
    decaying, healthy, completed = check_decay()

    st.markdown(f"""
    <div class="hero-banner">
        <h1>{greet()}, {user['name']}!</h1>
        <div class="subtitle">
            {user['exam']} | {user['branch']}
        </div>
    </div>
    """, unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)
    stats = [
        ("STREAK", progress.get("streak", 0), "Day Streak", "#4ade80"),
        ("SESSIONS", progress.get("total_sessions", 0), "Sessions Done", "#60a5fa"),
        ("RETENTION", f"{retention}%", "Retention", "#34d399"),
        ("DONE", len(completed), "Graduated", "#fbbf24"),
    ]

    for col, (icon, val, lbl, color) in zip([c1, c2, c3, c4], stats):
        with col:
            st.markdown(f"""
            <div class="stat-card">
                <div class="icon">{icon}</div>
                <div class="value" style="color:{color};">{val}</div>
                <div class="label">{lbl}</div>
                <div class="accent-bar" style="background:{color};"></div>
            </div>""", unsafe_allow_html=True)

    if decaying:
        n = len(decaying)
        st.markdown(f"""
        <div class="revise-card">
            <h3>Ready to Revise?</h3>
            <div class="meta">
                {n} topics due | {n * 7} questions | about {n * 5} min
            </div>
        </div>""", unsafe_allow_html=True)

        if st.button("Start Quiz Now", type="primary", use_container_width=True):
            st.session_state.page = "quiz"
            st.session_state.quiz_topic = decaying[0]["topic"]
            for k in ["quiz_questions", "quiz_parsed",
                      "quiz_answers", "quiz_submitted"]:
                if k in st.session_state:
                    del st.session_state[k]
            st.rerun()

    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown('<div class="section-title">Topic Health</div>',
                unsafe_allow_html=True)

    c1, c2 = st.columns(2)

    with c1:
        st.markdown("**Needs Attention**")
        if decaying:
            for t in decaying:
                ret = calculate_retention(t["topic"])
                css = "danger" if t["days_overdue"] > 2 else "warning"
                icon = "HIGH" if t["days_overdue"] > 2 else "DUE"
                msg = (f"{t['days_overdue']}d overdue"
                       if t["days_overdue"] > 2 else "Due today")
                st.markdown(f"""
                <div class="topic-card {css}">
                    <div class="t-name">{icon} {t['topic']}</div>
                    <div class="t-meta">{msg} | Retention: {ret}%</div>
                </div>""", unsafe_allow_html=True)
        else:
            st.success("All topics are healthy.")

    with c2:
        st.markdown("**Healthy Topics**")
        if healthy:
            for t in healthy:
                ret = calculate_retention(t["topic"])
                st.markdown(f"""
                <div class="topic-card success">
                    <div class="t-name">ACTIVE {t['topic']}</div>
                    <div class="t-meta">
                    Next in {t['days_until']}d | Retention: {ret}%
                    </div>
                </div>""", unsafe_allow_html=True)
        else:
            st.info("Add topics to get started.")

    if completed:
        st.markdown("<hr>", unsafe_allow_html=True)
        st.markdown('<div class="section-title">Graduated Topics</div>',
                    unsafe_allow_html=True)
        cols = st.columns(min(len(completed), 4))
        for i, topic in enumerate(completed):
            with cols[i % 4]:
                st.markdown(f"""
                <div class="topic-card success">
                    <div class="t-name">DONE {topic}</div>
                    <div class="t-meta">Permanently retained</div>
                </div>""", unsafe_allow_html=True)

    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown('<div class="section-title">Activity Wall | Last 7 Days</div>',
                unsafe_allow_html=True)

    activity = progress.get("daily_activity", {})
    cols = st.columns(7)
    for i, col in enumerate(cols):
        day = (datetime.now() - timedelta(days=6 - i)).strftime("%Y-%m-%d")
        short = (datetime.now() - timedelta(days=6 - i)).strftime("%a\n%d")
        sessions = activity.get(day, 0)
        with col:
            css = "active" if sessions > 0 else "empty"
            st.markdown(f"""
            <div class="activity-cell {css}">
                {short}<br>
                <b>{sessions}</b>
            </div>""", unsafe_allow_html=True)
