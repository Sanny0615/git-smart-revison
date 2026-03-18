import streamlit as st
from agents.progress_tracker import (
    load_schedule, calculate_retention,
    calculate_overall_retention, check_decay
)


def show():
    st.markdown("""
    <div class="hero-banner">
        <h1>Your Progress</h1>
        <div class="subtitle">
            Track your GATE preparation journey
        </div>
    </div>""", unsafe_allow_html=True)

    retention = calculate_overall_retention()
    decaying, healthy, completed = check_decay()
    total = len(decaying) + len(healthy) + len(completed)
    exam_ready = round(len(completed) / total * 100) if total > 0 else 0

    st.markdown(f"""
    <div class="progress-hero">
        <div style="color:#b9c8bd; font-size:0.82rem; font-weight:700;
        text-transform:uppercase; letter-spacing:0.1em; margin-bottom:0.55rem;">
        Current Status</div>
        <div style="font-size:3.3rem; font-weight:800; color:#f3fff5;
        line-height:1;">
            {exam_ready}%
            <span style="font-size:1.35rem; color:#4ade80; font-weight:700;">
            Exam Ready</span>
        </div>
        <div style="color:#b9c8bd; font-size:0.92rem; margin:0.85rem 0;">
        Overall retention: {retention}% | Graduate
        {max(0, 5 - len(completed))} more topics to reach the next milestone
        </div>
        <div class="progress-bar-outer">
            <div style="background:linear-gradient(90deg,#4ade80,#22c55e);
            width:{exam_ready}%; height:12px; border-radius:999px;"></div>
        </div>
        <div style="display:flex; justify-content:space-between;
        margin-top:0.45rem;">
            <span style="color:#7d9184; font-size:0.72rem;">NOVICE</span>
            <span style="color:#7d9184; font-size:0.72rem;">INTERMEDIATE</span>
            <span style="color:#7d9184; font-size:0.72rem;">EXPERT</span>
        </div>
    </div>""", unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)
    for col, val, lbl, color, icon in [
        (c1, len(healthy), "Active Topics", "#4ade80", "ACTIVE"),
        (c2, len(decaying), "Decaying", "#ef4444", "DUE"),
        (c3, len(completed), "Graduated", "#fbbf24", "DONE")
    ]:
        with col:
            st.markdown(f"""
            <div class="stat-card">
                <div class="icon">{icon}</div>
                <div class="value" style="color:{color};">{val}</div>
                <div class="label">{lbl}</div>
                <div class="accent-bar" style="background:{color};"></div>
            </div>""", unsafe_allow_html=True)

    schedule = load_schedule()
    if schedule:
        st.markdown("<hr>", unsafe_allow_html=True)
        st.markdown('<div class="section-title">Retention by Topic</div>',
                    unsafe_allow_html=True)

        import plotly.graph_objects as go

        topics, values, colors = [], [], []
        for topic in schedule:
            current_retention = calculate_retention(topic)
            topics.append(topic)
            values.append(current_retention if current_retention > 0 else 5)
            colors.append("#4ade80" if current_retention >= 70
                          else "#f59e0b" if current_retention >= 40
                          else "#ef4444")

        fig = go.Figure(go.Bar(
            x=values, y=topics, orientation="h",
            marker_color=colors,
            text=[f"{value}%" for value in values],
            textposition="auto",
            textfont=dict(size=13, color="#f3fff5", family="Plus Jakarta Sans")
        ))
        fig.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(12,18,14,1)",
            font=dict(color="#d7e5da", size=13, family="Plus Jakarta Sans"),
            xaxis=dict(
                range=[0, 100],
                gridcolor="rgba(255,255,255,0.08)",
                zerolinecolor="rgba(255,255,255,0.08)",
                tickfont=dict(size=12, color="#b9c8bd")
            ),
            yaxis=dict(
                gridcolor="rgba(255,255,255,0.04)",
                tickfont=dict(size=13, color="#f3fff5")
            ),
            height=max(220, len(topics) * 65),
            margin=dict(l=10, r=20, t=10, b=10),
            showlegend=False
        )
        st.plotly_chart(fig, use_container_width=True)

        st.markdown("<hr>", unsafe_allow_html=True)
        st.markdown('<div class="section-title">All Topics</div>',
                    unsafe_allow_html=True)

        for topic, data in schedule.items():
            current_retention = calculate_retention(topic)
            status = data.get("status", "active")
            level = data.get("current_level", 1)
            subject = data.get("subject", "")

            if status == "graduated":
                badge_class = "topic-pill-green"
                status_text = "GRADUATED"
            else:
                upcoming = [date for date in data.get("quiz_dates", [])
                            if date not in data.get("completed_sessions", [])]
                if upcoming:
                    from datetime import datetime as dt

                    next_date = dt.strptime(upcoming[0], "%Y-%m-%d")
                    days_left = (next_date - dt.now()).days
                    if days_left < 0:
                        badge_class = "topic-pill-red"
                        status_text = f"{abs(days_left)}D OVERDUE"
                    elif days_left == 0:
                        badge_class = "topic-pill-yellow"
                        status_text = "DUE TODAY"
                    else:
                        badge_class = "topic-pill-green"
                        status_text = f"DUE IN {days_left}D"
                else:
                    badge_class = "topic-pill-green"
                    status_text = "DONE"

            st.markdown(f"""
            <div class="topic-card success"
            style="display:flex; justify-content:space-between;
            align-items:center; flex-wrap:wrap; gap:0.7rem;">
                <div>
                    <div class="t-name">{topic}</div>
                    <div class="t-meta">
                    {subject} | Level {level}/3 | Retention: {current_retention}%
                    </div>
                </div>
                <span class="topic-pill {badge_class}">
                {status_text}</span>
            </div>""", unsafe_allow_html=True)
    else:
        st.info("Add topics to see your progress.")
