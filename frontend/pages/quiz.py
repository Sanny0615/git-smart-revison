import streamlit as st
from agents.progress_tracker import load_schedule, save_session
from agents.quiz_generator import generate_quiz


def parse_questions(text):
    questions = []
    current = {}
    options = []

    for line in text.strip().split("\n"):
        line = line.strip()
        if not line:
            continue
        if (line.startswith("Q") and ":" in line
                and len(line) < 250
                and line[1:3].replace("1", "").replace("2", "")
                .replace("3", "").replace("4", "")
                .replace("5", "").replace("6", "")
                .replace("7", "") in [":", " "]):
            if current and options:
                current["options"] = options
                questions.append(current)
            idx = line.index(":")
            current = {
                "num": line[:idx],
                "question": line[idx + 1:].strip(),
                "answer": "",
                "explanation": ""
            }
            options = []
        elif line.startswith(("A)", "B)", "C)", "D)")):
            options.append(line)
        elif line.lower().startswith("answer:"):
            current["answer"] = line.split(":", 1)[1].strip()
        elif line.lower().startswith("explanation:"):
            current["explanation"] = line.split(":", 1)[1].strip()

    if current and options:
        current["options"] = options
        questions.append(current)

    return questions


def show(load_database_fn):
    st.markdown("""
    <div class="hero-banner">
        <h1>Quiz Session</h1>
        <div class="subtitle">
            Questions generated from past GATE papers
        </div>
    </div>""", unsafe_allow_html=True)

    schedule = load_schedule()
    if not schedule:
        st.warning("No topics yet. Add topics first.")
        if st.button("Add Topic", type="primary"):
            st.session_state.page = "add_topic"
            st.rerun()
        return

    if "quiz_topic" not in st.session_state:
        st.markdown('<div class="section-title">Select Topic</div>',
                    unsafe_allow_html=True)
        selected = st.selectbox("", list(schedule.keys()),
                                label_visibility="collapsed")
        data = schedule.get(selected, {})
        level = data.get("current_level", 1)
        lnames = {1: "Foundational", 2: "Applied", 3: "Exam Level"}
        lcolors = {1: "#4ade80", 2: "#fbbf24", 3: "#f87171"}
        level_color = lcolors.get(level, "#4ade80")

        st.markdown(f"""
        <div class="topic-card success"
        style="border-left:4px solid {level_color}; padding:1.2rem;">
            <div style="display:flex; gap:0.75rem; align-items:center;
            flex-wrap:wrap;">
                <span style="font-size:1.05rem; font-weight:800;
                color:#f3fff5;">{selected}</span>
                <span style="background:{level_color}22; color:{level_color};
                padding:0.34rem 0.8rem; border-radius:999px; font-size:0.75rem;
                font-weight:800; border:1px solid {level_color};">
                Level {level} | {lnames[level]}</span>
                <span style="color:#b9c8bd; font-size:0.82rem;">
                {data.get('subject', 'General')}</span>
            </div>
            <div style="color:#b9c8bd; font-size:0.82rem; margin-top:0.75rem;">
            7 questions | AI-generated from GATE papers
            </div>
        </div>""", unsafe_allow_html=True)

        if st.button("Generate Questions", type="primary", use_container_width=True):
            st.session_state.quiz_topic = selected
            st.rerun()
        return

    topic = st.session_state.quiz_topic
    data = schedule.get(topic, {})
    level = data.get("current_level", 1)
    subject = data.get("subject", "General")
    lnames = {1: "Foundational", 2: "Applied", 3: "Exam Level"}
    lcolors = {1: "#4ade80", 2: "#fbbf24", 3: "#f87171"}
    level_color = lcolors.get(level, "#4ade80")

    st.markdown(f"""
    <div class="topic-card success"
    style="display:flex; gap:0.85rem; align-items:center; flex-wrap:wrap;
    border-left:4px solid {level_color}; margin-bottom:1rem;">
        <span style="font-size:1rem; font-weight:800; color:#f3fff5;">
        {topic}</span>
        <span style="background:{level_color}22; color:{level_color};
        padding:0.3rem 0.8rem; border-radius:999px; font-size:0.75rem;
        font-weight:800; border:1px solid {level_color};">
        Level {level} | {lnames[level]}</span>
        <span style="color:#b9c8bd; font-size:0.82rem;">{subject}</span>
    </div>""", unsafe_allow_html=True)

    if "quiz_questions" not in st.session_state:
        with st.spinner("Generating questions from GATE papers..."):
            try:
                collection = load_database_fn()
                raw = generate_quiz(topic, subject, level, collection)
                st.session_state.quiz_questions = raw
                st.session_state.quiz_parsed = parse_questions(raw)
                st.session_state.quiz_answers = {}
                st.session_state.quiz_submitted = False
            except Exception as e:
                st.error(f"Error: {e}")
                if st.button("Try Again"):
                    st.rerun()
                return

    parsed = st.session_state.get("quiz_parsed", [])
    submitted = st.session_state.get("quiz_submitted", False)

    if not parsed:
        st.error("Could not parse questions. Please try again.")
        if st.button("Regenerate Questions"):
            for k in ["quiz_questions", "quiz_parsed",
                      "quiz_answers", "quiz_submitted"]:
                if k in st.session_state:
                    del st.session_state[k]
            st.rerun()
        return

    answered = len(st.session_state.quiz_answers)
    progress_pct = answered / len(parsed)
    remaining = len(parsed) - answered

    st.markdown(f"""
    <div class="quiz-progress-card">
        <div class="quiz-progress-card__top">
            <div>
                <div class="quiz-progress-card__eyebrow">Quiz Progress</div>
                <div class="quiz-progress-card__title">
                    {answered} of {len(parsed)} answered
                </div>
            </div>
            <div class="quiz-progress-card__badge">
                {remaining} remaining
            </div>
        </div>
        <div class="quiz-progress-card__meta">
            Select one option for each question before submitting.
        </div>
    </div>""", unsafe_allow_html=True)

    st.progress(progress_pct,
                text=f"Answered {answered} of {len(parsed)} questions")

    st.markdown("<br>", unsafe_allow_html=True)

    for i, q in enumerate(parsed):
        qnum = q.get("num", f"Q{i + 1}")
        qtext = q.get("question", "")
        options = q.get("options", [])
        correct = q.get("answer", "").strip().upper()
        explanation = q.get("explanation", "")
        user_ans = st.session_state.quiz_answers.get(i)

        st.markdown(f"""
        <div class="quiz-wrapper">
            <div class="quiz-q-header">
                <div class="quiz-q-badge">{qnum}</div>
                <div class="quiz-q-status">
                    {"Answered" if user_ans else "Not answered"}
                </div>
            </div>
            <div class="quiz-q-text">{qtext}</div>
        </div>""", unsafe_allow_html=True)

        if not submitted:
            for opt in options:
                letter = opt[0].upper()
                is_selected = user_ans == letter
                option_text = opt[2:].strip()
                label = (f"{letter} | {option_text}"
                         if option_text else opt)
                if st.button(label, key=f"q{i}_opt_{letter}",
                             use_container_width=True,
                             type="primary" if is_selected else "secondary"):
                    st.session_state.quiz_answers[i] = letter
                    st.rerun()
        else:
            for opt in options:
                letter = opt[0].upper()
                is_correct_opt = correct and letter == correct[0]
                is_user = user_ans == letter

                if is_correct_opt:
                    st.markdown(f"""
                    <div class="opt-correct">Correct: {opt}</div>
                    """, unsafe_allow_html=True)
                elif is_user and not is_correct_opt:
                    st.markdown(f"""
                    <div class="opt-wrong">Your choice: {opt}</div>
                    """, unsafe_allow_html=True)
                else:
                    st.markdown(f"""
                    <div class="opt-neutral">{opt}</div>
                    """, unsafe_allow_html=True)

            if explanation:
                st.markdown(f"""
                <div class="explanation-box">Explanation: {explanation}</div>
                """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("<hr>", unsafe_allow_html=True)

    if not submitted:
        if answered < len(parsed):
            st.warning(
                f"Answer all {len(parsed)} questions to submit. "
                f"({answered}/{len(parsed)} done)"
            )
        if st.button(
            "Submit and See Results",
            type="primary",
            use_container_width=True,
            disabled=(answered < len(parsed))
        ):
            st.session_state.quiz_submitted = True
            st.rerun()
    else:
        correct_count = sum(
            1 for i, q in enumerate(parsed)
            if (st.session_state.quiz_answers.get(i, "") and
                q.get("answer", "").strip().upper() and
                st.session_state.quiz_answers[i] ==
                q["answer"].strip().upper()[0])
        )
        total = len(parsed)
        ret_pct = round((correct_count / total) * 100)
        color = ("#22c55e" if ret_pct >= 70
                 else "#f59e0b" if ret_pct >= 50
                 else "#ef4444")

        save_session(topic, subject, level, correct_count, total)

        st.markdown(f"""
        <div class="completion-card">
            <h2 style="font-size:2.1rem; font-weight:800; color:#f3fff5;
            margin:0;">Session Complete</h2>
            <p style="color:#b9c8bd; font-size:1rem; margin:0.6rem 0 1.6rem 0;">
            Review your results and keep building retention.
            </p>
            <div style="display:flex; gap:2rem; justify-content:center;
            flex-wrap:wrap;">
                <div>
                    <div style="font-size:2.3rem; font-weight:800;
                    color:#f3fff5;">{correct_count}/{total}</div>
                    <div style="color:#b9c8bd; font-size:0.78rem;
                    font-weight:700;">SCORE</div>
                </div>
                <div>
                    <div style="font-size:2.3rem; font-weight:800;
                    color:{color};">{ret_pct}%</div>
                    <div style="color:#b9c8bd; font-size:0.78rem;
                    font-weight:700;">RETENTION</div>
                </div>
            </div>
        </div>""", unsafe_allow_html=True)

        if ret_pct >= 70:
            st.success("Excellent work. You are ready for the next level.")
        elif ret_pct >= 50:
            st.info("Good effort. A little more practice will help.")
        else:
            st.warning("Review this topic once more and try again.")

        c1, c2 = st.columns(2)
        with c1:
            if st.button("Back to Home", type="primary", use_container_width=True):
                st.session_state.page = "home"
                for k in ["quiz_questions", "quiz_parsed", "quiz_answers",
                          "quiz_submitted", "quiz_topic"]:
                    if k in st.session_state:
                        del st.session_state[k]
                st.rerun()
        with c2:
            if st.button("Try Another Topic", use_container_width=True):
                for k in ["quiz_questions", "quiz_parsed", "quiz_answers",
                          "quiz_submitted", "quiz_topic"]:
                    if k in st.session_state:
                        del st.session_state[k]
                st.rerun()
