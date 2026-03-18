import streamlit as st
from datetime import datetime, timedelta
from agents.scheduler import add_topic
from agents.progress_tracker import load_schedule


def show():
    st.markdown("""
    <div class="hero-banner">
        <h1>Add a New Topic</h1>
        <div class="subtitle">
            Build a revision plan automatically with spaced repetition
        </div>
    </div>""", unsafe_allow_html=True)

    st.markdown("""
    <div class="form-shell">
        <div class="form-shell__header">
            <div class="form-shell__eyebrow">Topic Setup</div>
            <div class="form-shell__title">Create a clean revision entry</div>
            <div class="form-shell__copy">
                Enter the topic you studied and choose the subject area.
                A revision schedule will appear instantly before you save it.
            </div>
        </div>
    </div>""", unsafe_allow_html=True)

    c1, c2 = st.columns(2)
    with c1:
        st.markdown("""
        <div class="field-hint">
            Use a short, specific name so it is easy to recognize later.
        </div>""", unsafe_allow_html=True)
        topic = st.text_input(
            "Topic name",
            placeholder="e.g. Logic Gates, Deadlock, B-Trees"
        )
    with c2:
        st.markdown("""
        <div class="field-hint">
            Pick the subject that best matches this topic.
        </div>""", unsafe_allow_html=True)
        subject = st.selectbox("Subject", [
            "Digital Logic", "Operating Systems", "DBMS",
            "Computer Networks", "Data Structures", "Algorithms",
            "Theory of Computation", "Computer Organization",
            "Compiler Design", "Discrete Mathematics"
        ])

    clean_topic = topic.strip()

    if not clean_topic:
        st.info("Enter a topic name to preview the spaced revision schedule.")

    if topic:
        st.markdown('<div class="section-title">Your Revision Schedule</div>',
                    unsafe_allow_html=True)

        intervals = [1, 3, 7, 14, 21, 30, 60]
        labels = ["Today", "Review 1", "Review 2", "Review 3",
                  "Mastery", "Retention 1", "Retention 2"]
        cols = st.columns(7)

        for i, (interval, label) in enumerate(zip(intervals, labels)):
            with cols[i]:
                date = (datetime.now() + timedelta(days=interval)).strftime("%b %d")
                css = "first" if i == 0 else "rest"
                st.markdown(f"""
                <div class="schedule-day {css}">
                    <div class="day-num">DAY {interval}</div>
                    <div class="day-label">{label}</div>
                    <div class="day-date">{date}</div>
                </div>""", unsafe_allow_html=True)

        st.markdown("""
        <div class="topic-card success" style="margin-top:1rem;">
            <div class="t-name">Scientifically Scheduled</div>
            <div class="t-meta">
                This plan is spaced for long-term retention using the
                Ebbinghaus forgetting curve approach.
            </div>
        </div>""", unsafe_allow_html=True)

        if st.button("Schedule Revision", type="primary", use_container_width=True):
            if not clean_topic:
                st.error("Topic name cannot be empty.")
                return

            schedule = load_schedule()
            if clean_topic.lower() in [k.lower() for k in schedule.keys()]:
                st.warning(f"'{clean_topic}' is already in your schedule.")
            else:
                add_topic(clean_topic, subject)
                st.success(f"'{clean_topic}' added. Your first quiz is ready today.")
                st.balloons()
