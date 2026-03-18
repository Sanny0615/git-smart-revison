import streamlit as st
import sys
import os

sys.path.append(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)

from agents.progress_tracker import load_user, load_progress
from agents.rag_setup import get_collection
from frontend.style import load_css
from frontend.pages import home, add_topic, quiz, progress, history

st.set_page_config(
    page_title="Smart Revision System",
    page_icon="SR",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown(load_css(), unsafe_allow_html=True)


@st.cache_resource
def load_database():
    return get_collection()


def sidebar():
    with st.sidebar:
        st.markdown("""
        <div class="sidebar-brand">
            <div class="sidebar-brand__logo">SR</div>
            <div class="sidebar-brand__title">Smart Revision</div>
            <div class="sidebar-brand__subtitle">AI | Spaced Repetition</div>
        </div>""", unsafe_allow_html=True)

        st.markdown("""
        <div class="sidebar-divider"></div>
        """, unsafe_allow_html=True)

        user = load_user()
        progress = load_progress()

        st.markdown(f"""
        <div class="sidebar-user-card">
            <div class="sidebar-user-card__top">
                <div class="sidebar-user-card__avatar">
                {user['name'][0].upper()}</div>
                <div>
                    <div class="sidebar-user-card__name">
                    {user['name']}</div>
                    <div class="sidebar-user-card__meta">
                    {user['exam']}</div>
                </div>
            </div>
            <div class="sidebar-user-card__stats">
                <div class="sidebar-metric">
                    <div class="sidebar-metric__value">
                    {progress.get('streak', 0)}</div>
                    <div class="sidebar-metric__label">Streak</div>
                </div>
                <div class="sidebar-metric">
                    <div class="sidebar-metric__value">
                    {progress.get('total_sessions', 0)}</div>
                    <div class="sidebar-metric__label">Sessions</div>
                </div>
            </div>
        </div>""", unsafe_allow_html=True)

        st.markdown("""
        <div class="sidebar-section-label">Navigation</div>
        """, unsafe_allow_html=True)

        pages = [
            ("01", "Home", "home"),
            ("02", "Add Topic", "add_topic"),
            ("03", "Start Quiz", "quiz"),
            ("04", "Progress", "progress"),
            ("05", "History", "history"),
        ]

        for icon, label, key in pages:
            active = st.session_state.get("page", "home") == key
            if st.button(
                f"{icon}  {label}",
                use_container_width=True,
                type="primary" if active else "secondary",
                key=f"nav_{key}"
            ):
                st.session_state.page = key
                if key == "quiz":
                    for k in ["quiz_questions", "quiz_parsed",
                              "quiz_answers", "quiz_submitted", "quiz_topic"]:
                        if k in st.session_state:
                            del st.session_state[k]
                st.rerun()

        st.markdown("<br><br>", unsafe_allow_html=True)
        st.markdown("""
        <div class="sidebar-footer">
            <div class="sidebar-footer__title">Research Grounding</div>
            Ebbinghaus Forgetting Curve<br>
            Shen and Tamkin (2024)
        </div>""", unsafe_allow_html=True)


def main():
    if "page" not in st.session_state:
        st.session_state.page = "home"

    sidebar()

    page = st.session_state.page

    if page == "home":
        home.show()
    elif page == "add_topic":
        add_topic.show()
    elif page == "quiz":
        quiz.show(load_database)
    elif page == "progress":
        progress.show()
    elif page == "history":
        history.show()


if __name__ == "__main__":
    main()
