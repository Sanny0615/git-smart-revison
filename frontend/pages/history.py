import streamlit as st
from agents.progress_tracker import load_history, load_progress


def show():
    st.markdown("""
    <div class="hero-banner">
        <h1>Session History</h1>
        <div class="subtitle">
            A complete view of your revision journey
        </div>
    </div>""", unsafe_allow_html=True)

    history = load_history()
    progress = load_progress()

    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown(f"""
        <div class="stat-card">
            <div class="icon">SESSIONS</div>
            <div class="value">{progress.get('total_sessions', 0)}</div>
            <div class="label">Total Sessions</div>
            <div class="accent-bar" style="background:#4ade80;"></div>
        </div>""", unsafe_allow_html=True)
    with c2:
        avg = 0
        if history:
            avg = round(sum(s.get("retention", 0) for s in history) / len(history))
        st.markdown(f"""
        <div class="stat-card">
            <div class="icon">AVERAGE</div>
            <div class="value">{avg}%</div>
            <div class="label">Avg Retention</div>
            <div class="accent-bar" style="background:#34d399;"></div>
        </div>""", unsafe_allow_html=True)
    with c3:
        best = 0
        if history:
            best = max(s.get("retention", 0) for s in history)
        st.markdown(f"""
        <div class="stat-card">
            <div class="icon">BEST</div>
            <div class="value">{best}%</div>
            <div class="label">Best Session</div>
            <div class="accent-bar" style="background:#fbbf24;"></div>
        </div>""", unsafe_allow_html=True)

    st.markdown("<hr>", unsafe_allow_html=True)

    if not history:
        st.info("No sessions yet. Start your first quiz.")
        if st.button("Start Quiz", type="primary"):
            st.session_state.page = "quiz"
            st.rerun()
        return

    st.markdown('<div class="section-title">All Sessions</div>',
                unsafe_allow_html=True)

    for session in reversed(history):
        ret = session.get("retention", 0)
        if ret >= 70:
            badge = "badge-green"
            border = "#4ade80"
        elif ret >= 40:
            badge = "badge-yellow"
            border = "#f59e0b"
        else:
            badge = "badge-red"
            border = "#ef4444"

        st.markdown(f"""
        <div class="session-item" style="border-left:4px solid {border};">
            <div style="display:flex; justify-content:space-between;
            align-items:center; margin-bottom:0.7rem; flex-wrap:wrap; gap:0.7rem;">
                <div>
                    <span style="font-size:1rem; font-weight:800;
                    color:#f3fff5;">{session['topic']}</span>
                    <span style="color:#b9c8bd; font-size:0.82rem;
                    margin-left:0.65rem;">{session['subject']}</span>
                </div>
                <span class="retention-badge {badge}">
                {ret}% Retention</span>
            </div>
            <div style="display:flex; gap:1rem; flex-wrap:wrap;">
                <span style="color:#b9c8bd; font-size:0.82rem;">
                Date: {session['date']}</span>
                <span style="color:#b9c8bd; font-size:0.82rem;">
                Time: {session.get('time', '')}</span>
                <span style="color:#b9c8bd; font-size:0.82rem;">
                Level {session['level']}/3</span>
                <span style="font-size:0.82rem; font-weight:700;
                color:#f3fff5;">
                Score {session['score']}/{session['total']}</span>
            </div>
        </div>""", unsafe_allow_html=True)
