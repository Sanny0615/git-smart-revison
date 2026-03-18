def load_css():
    return """
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Space+Grotesk:wght@500;700&display=swap');

:root {
    --bg-primary: #050805;
    --bg-secondary: #0b120d;
    --panel: #101712;
    --panel-soft: #141d17;
    --panel-strong: #18231b;
    --border: rgba(110, 231, 140, 0.16);
    --border-strong: rgba(110, 231, 140, 0.35);
    --text-primary: #f3fff5;
    --text-secondary: #b9c8bd;
    --text-muted: #7d9184;
    --text-strong-dark: #041107;
    --accent: #4ade80;
    --accent-strong: #22c55e;
    --accent-soft: rgba(74, 222, 128, 0.14);
    --danger: #f87171;
    --warning: #fbbf24;
    --shadow: 0 18px 40px rgba(0, 0, 0, 0.35);
}

html, body, [class*="css"] {
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    color: var(--text-primary) !important;
}

.stApp {
    background:
        radial-gradient(circle at top right, rgba(34, 197, 94, 0.12), transparent 24%),
        radial-gradient(circle at top left, rgba(74, 222, 128, 0.10), transparent 20%),
        linear-gradient(180deg, #040604 0%, #081009 45%, #050805 100%) !important;
    color: var(--text-primary) !important;
}

.block-container {
    padding-top: 2.2rem !important;
    padding-bottom: 3rem !important;
    max-width: 1220px !important;
}

[data-testid="stHeader"] {
    background: rgba(5, 8, 5, 0.78) !important;
}

[data-testid="stToolbar"] {
    right: 1rem !important;
}

section[data-testid="stSidebar"] {
    background:
        linear-gradient(180deg, rgba(8, 12, 9, 0.98) 0%, rgba(9, 15, 11, 0.98) 100%) !important;
    border-right: 1px solid rgba(110, 231, 140, 0.10) !important;
}

section[data-testid="stSidebar"] [data-testid="stSidebarUserContent"] {
    padding-top: 1rem !important;
    padding-left: 1rem !important;
    padding-right: 1rem !important;
}

section[data-testid="stSidebar"] * {
    color: var(--text-primary) !important;
}

section[data-testid="stSidebar"] .stButton > button {
    background: linear-gradient(180deg, rgba(255, 255, 255, 0.035), rgba(255, 255, 255, 0.015)) !important;
    color: var(--text-primary) !important;
    -webkit-text-fill-color: var(--text-primary) !important;
    border: 1px solid rgba(255, 255, 255, 0.08) !important;
    border-radius: 16px !important;
    font-weight: 700 !important;
    padding: 0.95rem 1rem !important;
    margin: 0.28rem 0 !important;
    text-align: left !important;
    justify-content: flex-start !important;
    min-height: 3.2rem !important;
    box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.03) !important;
}

section[data-testid="stSidebar"] .stButton > button:hover {
    border-color: var(--border-strong) !important;
    background: linear-gradient(180deg, rgba(74, 222, 128, 0.12), rgba(74, 222, 128, 0.05)) !important;
    color: var(--text-primary) !important;
    -webkit-text-fill-color: var(--text-primary) !important;
    transform: translateX(2px) !important;
}

section[data-testid="stSidebar"] .stButton > button[kind="primary"] {
    background: linear-gradient(135deg, var(--accent), var(--accent-strong)) !important;
    color: var(--text-strong-dark) !important;
    -webkit-text-fill-color: var(--text-strong-dark) !important;
    border: none !important;
    box-shadow: 0 10px 24px rgba(34, 197, 94, 0.24) !important;
}

section[data-testid="stSidebar"] .stButton > button[kind="primary"]:hover {
    background: linear-gradient(135deg, #69eb96, #29d164) !important;
    color: var(--text-strong-dark) !important;
    -webkit-text-fill-color: var(--text-strong-dark) !important;
    transform: translateX(2px) !important;
}

.sidebar-brand {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 0.45rem;
    padding: 0.8rem 0 1.1rem;
}

.sidebar-brand__logo {
    width: 4rem;
    height: 4rem;
    border-radius: 1.15rem;
    display: flex;
    align-items: center;
    justify-content: center;
    background: linear-gradient(135deg, rgba(74, 222, 128, 0.95), rgba(34, 197, 94, 0.92));
    color: #041107 !important;
    font-family: 'Space Grotesk', sans-serif !important;
    font-size: 1.35rem;
    font-weight: 800;
    box-shadow: 0 16px 34px rgba(34, 197, 94, 0.22);
}

.sidebar-brand__title {
    font-family: 'Space Grotesk', sans-serif !important;
    font-size: 1.35rem;
    font-weight: 700;
    color: var(--text-primary) !important;
}

.sidebar-brand__subtitle {
    color: #8ff0ab !important;
    font-size: 0.72rem;
    font-weight: 700;
    letter-spacing: 0.14em;
    text-transform: uppercase;
}

.sidebar-divider {
    height: 1px;
    margin: 0.15rem 0 1rem;
    background: linear-gradient(90deg, transparent, rgba(110, 231, 140, 0.32), transparent);
}

.sidebar-user-card {
    background: linear-gradient(180deg, rgba(74, 222, 128, 0.09), rgba(74, 222, 128, 0.04));
    border: 1px solid rgba(74, 222, 128, 0.18);
    border-radius: 18px;
    padding: 1rem;
    margin-bottom: 1.1rem;
    box-shadow: 0 16px 28px rgba(0, 0, 0, 0.22);
}

.sidebar-user-card__top {
    display: flex;
    align-items: center;
    gap: 0.8rem;
}

.sidebar-user-card__avatar {
    width: 2.8rem;
    height: 2.8rem;
    border-radius: 0.9rem;
    display: flex;
    align-items: center;
    justify-content: center;
    background: linear-gradient(135deg, var(--accent), var(--accent-strong));
    color: #041107 !important;
    font-size: 1.05rem;
    font-weight: 800;
}

.sidebar-user-card__name {
    color: var(--text-primary) !important;
    font-size: 0.96rem;
    font-weight: 800;
}

.sidebar-user-card__meta {
    color: #8ff0ab !important;
    font-size: 0.72rem;
    font-weight: 700;
    margin-top: 0.15rem;
    text-transform: uppercase;
    letter-spacing: 0.08em;
}

.sidebar-user-card__stats {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 0.7rem;
    margin-top: 0.95rem;
    padding-top: 0.9rem;
    border-top: 1px solid rgba(74, 222, 128, 0.12);
}

.sidebar-metric {
    background: rgba(255, 255, 255, 0.03);
    border: 1px solid rgba(255, 255, 255, 0.05);
    border-radius: 14px;
    padding: 0.7rem 0.5rem;
    text-align: center;
}

.sidebar-metric__value {
    color: var(--text-primary) !important;
    font-size: 1rem;
    font-weight: 800;
}

.sidebar-metric__label {
    color: var(--text-muted) !important;
    font-size: 0.64rem;
    font-weight: 700;
    margin-top: 0.2rem;
    text-transform: uppercase;
    letter-spacing: 0.08em;
}

.sidebar-section-label {
    color: var(--text-secondary) !important;
    font-size: 0.7rem;
    font-weight: 800;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    margin: 0.1rem 0 0.45rem;
    padding-left: 0.2rem;
}

.sidebar-footer {
    color: var(--text-muted) !important;
    font-size: 0.72rem;
    line-height: 1.8;
    border-top: 1px solid rgba(255, 255, 255, 0.08);
    padding-top: 1rem;
}

.sidebar-footer__title {
    color: var(--accent) !important;
    font-weight: 800;
    margin-bottom: 0.25rem;
    font-size: 0.74rem;
    text-transform: uppercase;
    letter-spacing: 0.12em;
}

.form-shell {
    background: linear-gradient(180deg, rgba(16, 23, 18, 0.96), rgba(11, 17, 13, 0.98));
    border: 1px solid var(--border);
    border-radius: 20px;
    padding: 1.35rem 1.4rem;
    margin-bottom: 1.2rem;
    box-shadow: var(--shadow);
}

.form-shell__header {
    display: flex;
    flex-direction: column;
    gap: 0.35rem;
}

.form-shell__eyebrow {
    color: #8ff0ab !important;
    font-size: 0.72rem;
    font-weight: 800;
    letter-spacing: 0.14em;
    text-transform: uppercase;
}

.form-shell__title {
    color: var(--text-primary) !important;
    font-family: 'Space Grotesk', sans-serif !important;
    font-size: 1.18rem;
    font-weight: 700;
}

.form-shell__copy {
    color: var(--text-secondary) !important;
    font-size: 0.9rem;
    line-height: 1.7;
    max-width: 48rem;
}

.field-hint {
    color: var(--text-muted) !important;
    font-size: 0.78rem;
    margin: 0.05rem 0 0.45rem;
    line-height: 1.5;
}

h1, h2, h3, h4, h5, h6, p, label, span, div {
    color: inherit;
}

[data-testid="stMarkdownContainer"] p,
[data-testid="stMarkdownContainer"] li,
.stAlert,
.stCaption,
.stText,
.st-emotion-cache-16txtl3,
.st-emotion-cache-10trblm,
.st-emotion-cache-ue6h4q,
.st-emotion-cache-1c7y2kd {
    color: var(--text-primary) !important;
}

.hero-banner,
.progress-hero,
.quiz-wrapper,
.session-item,
.topic-card,
.stat-card,
.completion-card,
.revise-card {
    box-shadow: var(--shadow);
}

.hero-banner {
    background:
        radial-gradient(circle at top right, rgba(74, 222, 128, 0.18), transparent 28%),
        linear-gradient(135deg, #0a120c 0%, #101912 55%, #0d1610 100%);
    border: 1px solid var(--border);
    border-radius: 24px;
    padding: 2rem 2.2rem;
    margin-bottom: 1.6rem;
    position: relative;
    overflow: hidden;
}

.hero-banner::before {
    content: '';
    position: absolute;
    inset: auto -70px -70px auto;
    width: 220px;
    height: 220px;
    border-radius: 50%;
    background: radial-gradient(circle, rgba(74, 222, 128, 0.16) 0%, transparent 70%);
}

.hero-banner h1 {
    color: var(--text-primary) !important;
    font-family: 'Space Grotesk', sans-serif !important;
    font-size: 2rem !important;
    font-weight: 700 !important;
    line-height: 1.15 !important;
    margin: 0 !important;
}

.hero-banner .subtitle {
    color: #8ff0ab !important;
    font-size: 0.95rem;
    font-weight: 600;
    margin-top: 0.6rem;
}

.stat-card {
    background: linear-gradient(180deg, rgba(16, 23, 18, 0.96), rgba(12, 18, 14, 0.98));
    border: 1px solid var(--border);
    border-radius: 18px;
    padding: 1.3rem 1rem;
    text-align: center;
    position: relative;
    overflow: hidden;
    min-height: 150px;
}

.stat-card:hover {
    border-color: var(--border-strong);
    transform: translateY(-2px);
    color: var(--text-primary);
}

.stat-card .icon {
    font-size: 1.6rem;
    margin-bottom: 0.5rem;
}

.stat-card .value {
    font-size: 1.9rem;
    font-weight: 800;
    color: var(--text-primary);
    line-height: 1.1;
}

.stat-card .label {
    font-size: 0.76rem;
    color: var(--text-secondary);
    font-weight: 700;
    margin-top: 0.5rem;
    text-transform: uppercase;
    letter-spacing: 0.08em;
}

.stat-card .accent-bar {
    position: absolute;
    bottom: 0;
    left: 0;
    right: 0;
    height: 3px;
}

.revise-card,
.progress-hero,
.quiz-wrapper,
.session-item,
.topic-card,
.completion-card {
    background: linear-gradient(180deg, rgba(16, 23, 18, 0.96), rgba(11, 17, 13, 0.98));
    border: 1px solid var(--border);
}

.revise-card {
    border-radius: 20px;
    padding: 1.5rem 1.75rem;
    margin: 1.25rem 0;
    position: relative;
    overflow: hidden;
}

.revise-card::after {
    content: 'REVISE';
    position: absolute;
    right: 1.5rem;
    top: 50%;
    transform: translateY(-50%);
    font-size: 1.2rem;
    letter-spacing: 0.22em;
    color: rgba(74, 222, 128, 0.14);
    font-weight: 800;
}

.revise-card h3 {
    color: var(--text-primary) !important;
    font-size: 1.25rem !important;
    font-weight: 800 !important;
    margin: 0 !important;
}

.revise-card .meta {
    color: var(--text-secondary);
    font-size: 0.9rem;
    margin-top: 0.45rem;
}

.topic-pill {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    padding: 0.36rem 0.85rem;
    border-radius: 999px;
    font-size: 0.7rem;
    font-weight: 800;
    letter-spacing: 0.08em;
    text-transform: uppercase;
}

.topic-pill-red {
    background: rgba(248, 113, 113, 0.12);
    color: #fecaca;
    border: 1px solid rgba(248, 113, 113, 0.4);
}

.topic-pill-yellow {
    background: rgba(251, 191, 36, 0.12);
    color: #fde68a;
    border: 1px solid rgba(251, 191, 36, 0.34);
}

.topic-pill-green {
    background: rgba(74, 222, 128, 0.12);
    color: #bbf7d0;
    border: 1px solid rgba(74, 222, 128, 0.34);
}

.topic-card {
    border-radius: 16px;
    padding: 1rem 1.05rem;
    margin: 0.55rem 0;
}

.topic-card:hover,
.session-item:hover,
.quiz-wrapper:hover {
    border-color: var(--border-strong);
    color: var(--text-primary);
}

.topic-card.danger {
    border-left: 4px solid var(--danger);
}

.topic-card.warning {
    border-left: 4px solid var(--warning);
}

.topic-card.success {
    border-left: 4px solid var(--accent);
}

.topic-card .t-name {
    font-size: 0.98rem;
    font-weight: 800;
    color: var(--text-primary);
}

.topic-card .t-meta {
    font-size: 0.8rem;
    color: var(--text-secondary);
    margin-top: 0.3rem;
    line-height: 1.55;
}

.activity-cell {
    border-radius: 12px;
    padding: 0.9rem 0.25rem;
    text-align: center;
    font-size: 0.7rem;
    font-weight: 700;
    border: 1px solid var(--border);
}

.activity-cell.active {
    background: linear-gradient(135deg, var(--accent), var(--accent-strong));
    color: #041107;
}

.activity-cell.empty {
    background: rgba(255, 255, 255, 0.03);
    color: var(--text-muted);
}

.schedule-day {
    border-radius: 16px;
    padding: 0.95rem 0.5rem;
    text-align: center;
    margin: 0.2rem;
    border: 1px solid var(--border);
    background: linear-gradient(180deg, rgba(16, 23, 18, 0.98), rgba(11, 17, 13, 0.98));
    min-height: 108px;
}

.schedule-day.first {
    background: linear-gradient(135deg, rgba(13, 46, 24, 0.98), rgba(11, 90, 34, 0.85));
    border: 1px solid rgba(110, 231, 140, 0.4);
}

.schedule-day.rest {
    background: linear-gradient(180deg, rgba(16, 23, 18, 0.96), rgba(10, 16, 12, 0.98));
}

.schedule-day .day-num {
    color: #9df5b9;
    font-size: 0.7rem;
    font-weight: 800;
    letter-spacing: 0.08em;
}

.schedule-day .day-label {
    color: var(--text-secondary);
    font-size: 0.7rem;
    margin: 0.3rem 0;
}

.schedule-day .day-date {
    color: var(--text-primary);
    font-size: 0.96rem;
    font-weight: 700;
}

.quiz-wrapper {
    border-radius: 20px;
    padding: 1.55rem 1.65rem;
    margin: 0.9rem 0 0.7rem;
}

.quiz-progress-card {
    background: linear-gradient(180deg, rgba(16, 23, 18, 0.96), rgba(11, 17, 13, 0.98));
    border: 1px solid var(--border);
    border-radius: 18px;
    padding: 1rem 1.1rem;
    margin: 0.4rem 0 0.8rem;
    box-shadow: var(--shadow);
}

.quiz-progress-card__top {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 0.8rem;
    flex-wrap: wrap;
}

.quiz-progress-card__eyebrow {
    color: #8ff0ab !important;
    font-size: 0.72rem;
    font-weight: 800;
    letter-spacing: 0.14em;
    text-transform: uppercase;
}

.quiz-progress-card__title {
    color: var(--text-primary) !important;
    font-family: 'Space Grotesk', sans-serif !important;
    font-size: 1.05rem;
    font-weight: 700;
    margin-top: 0.2rem;
}

.quiz-progress-card__badge {
    background: rgba(74, 222, 128, 0.10);
    border: 1px solid rgba(74, 222, 128, 0.26);
    border-radius: 999px;
    color: #c9ffd6 !important;
    font-size: 0.76rem;
    font-weight: 800;
    padding: 0.4rem 0.8rem;
}

.quiz-progress-card__meta {
    color: var(--text-secondary) !important;
    font-size: 0.84rem;
    margin-top: 0.6rem;
}

.quiz-q-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 0.8rem;
    flex-wrap: wrap;
}

.quiz-q-badge {
    background: rgba(74, 222, 128, 0.12);
    border: 1px solid rgba(74, 222, 128, 0.28);
    color: #a7f3be;
    padding: 0.34rem 0.82rem;
    border-radius: 999px;
    font-size: 0.72rem;
    font-weight: 800;
    display: inline-block;
    margin-bottom: 0.9rem;
    letter-spacing: 0.08em;
}

.quiz-q-status {
    color: var(--text-secondary) !important;
    font-size: 0.74rem;
    font-weight: 700;
    letter-spacing: 0.04em;
}

.quiz-q-text {
    font-size: 1.08rem;
    font-weight: 700;
    color: var(--text-primary);
    line-height: 1.7;
}

.stProgress {
    margin-bottom: 1.2rem !important;
}

.stProgress div[data-testid="stProgressBar"] {
    height: 0.85rem !important;
    border-radius: 999px !important;
    overflow: hidden !important;
}

.stProgress > div {
    gap: 0.45rem !important;
}

.opt-correct,
.opt-wrong,
.opt-neutral,
.explanation-box {
    border-radius: 14px;
    padding: 0.95rem 1rem;
    margin: 0.45rem 0;
    font-size: 0.92rem;
}

.opt-correct {
    background: rgba(34, 197, 94, 0.12);
    border: 1px solid rgba(34, 197, 94, 0.42);
    color: #bbf7d0;
    font-weight: 700;
}

.opt-wrong {
    background: rgba(248, 113, 113, 0.12);
    border: 1px solid rgba(248, 113, 113, 0.42);
    color: #fecaca;
    font-weight: 700;
}

.opt-neutral {
    background: rgba(255, 255, 255, 0.03);
    border: 1px solid rgba(255, 255, 255, 0.06);
    color: var(--text-secondary);
}

.explanation-box {
    background: rgba(74, 222, 128, 0.08);
    border: 1px solid rgba(74, 222, 128, 0.18);
    color: #d8ffe1;
    font-weight: 500;
}

.completion-card {
    border-radius: 24px;
    padding: 2.6rem 2rem;
    text-align: center;
    margin: 1.25rem 0;
}

.progress-hero {
    border-radius: 24px;
    padding: 2rem 2.2rem;
    margin-bottom: 1.45rem;
}

.progress-bar-outer {
    background: rgba(255, 255, 255, 0.06);
    border-radius: 999px;
    height: 12px;
    margin-top: 1rem;
    overflow: hidden;
    border: 1px solid rgba(255, 255, 255, 0.04);
}

.session-item {
    border-radius: 16px;
    padding: 1.1rem 1.2rem;
    margin: 0.75rem 0;
}

.retention-badge {
    padding: 0.34rem 0.82rem;
    border-radius: 999px;
    font-size: 0.74rem;
    font-weight: 800;
}

.badge-green {
    background: rgba(34, 197, 94, 0.12);
    color: #bbf7d0;
}

.badge-yellow {
    background: rgba(251, 191, 36, 0.12);
    color: #fde68a;
}

.badge-red {
    background: rgba(248, 113, 113, 0.12);
    color: #fecaca;
}

div.stButton > button {
    border-radius: 14px !important;
    font-weight: 700 !important;
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    transition: all 0.2s ease !important;
    padding: 0.78rem 1rem !important;
    border: 1px solid rgba(255, 255, 255, 0.08) !important;
    color: var(--text-primary) !important;
    -webkit-text-fill-color: currentColor !important;
}

div.stButton > button[kind="primary"] {
    background: linear-gradient(135deg, var(--accent), var(--accent-strong)) !important;
    color: var(--text-strong-dark) !important;
    -webkit-text-fill-color: var(--text-strong-dark) !important;
    border: none !important;
    box-shadow: 0 10px 24px rgba(34, 197, 94, 0.24) !important;
}

div.stButton > button[kind="primary"]:hover {
    color: var(--text-strong-dark) !important;
    -webkit-text-fill-color: var(--text-strong-dark) !important;
    transform: translateY(-1px) !important;
    box-shadow: 0 14px 28px rgba(34, 197, 94, 0.28) !important;
}

div.stButton > button[kind="secondary"] {
    background: rgba(255, 255, 255, 0.03) !important;
    color: var(--text-primary) !important;
    -webkit-text-fill-color: var(--text-primary) !important;
    border: 1px solid rgba(255, 255, 255, 0.08) !important;
}

div.stButton > button[kind="secondary"]:hover {
    background: rgba(74, 222, 128, 0.06) !important;
    border-color: var(--border-strong) !important;
    color: var(--text-primary) !important;
    -webkit-text-fill-color: var(--text-primary) !important;
}

[data-testid="stVerticalBlock"] > div:has(> div.stButton) {
    width: 100%;
}

[data-testid="stVerticalBlock"] .stButton {
    width: 100%;
}

[data-testid="stVerticalBlock"] .stButton > button {
    min-height: 3.65rem !important;
}

section[data-testid="stSidebar"] .stButton > button {
    min-height: 3.2rem !important;
}

section[data-testid="stSidebar"] .stButton > button[kind="secondary"] {
    background: linear-gradient(180deg, rgba(255, 255, 255, 0.035), rgba(255, 255, 255, 0.015)) !important;
}

.stApp .stButton > button[kind="secondary"] {
    background: linear-gradient(180deg, rgba(24, 35, 27, 0.98), rgba(16, 23, 18, 0.98)) !important;
    color: var(--text-primary) !important;
    -webkit-text-fill-color: var(--text-primary) !important;
    border: 1px solid rgba(255, 255, 255, 0.10) !important;
    border-radius: 16px !important;
    text-align: left !important;
    justify-content: flex-start !important;
    padding: 1rem 1rem !important;
    box-shadow: var(--shadow);
}

.stApp .stButton > button[kind="secondary"]:hover {
    background: linear-gradient(180deg, rgba(29, 43, 32, 0.98), rgba(18, 27, 20, 0.98)) !important;
    border-color: rgba(110, 231, 140, 0.30) !important;
    color: var(--text-primary) !important;
    -webkit-text-fill-color: var(--text-primary) !important;
    transform: translateY(-1px) !important;
}

.stApp .stButton > button[kind="primary"] {
    text-align: left !important;
    justify-content: flex-start !important;
    color: var(--text-strong-dark) !important;
    -webkit-text-fill-color: var(--text-strong-dark) !important;
}

.stTextInput > label,
.stSelectbox > label,
.stMultiSelect > label,
.stTextArea > label,
.stDateInput > label,
.stNumberInput > label,
[data-testid="stWidgetLabel"] p {
    color: var(--text-primary) !important;
    font-weight: 700 !important;
}

.stTextInput input,
.stTextArea textarea,
.stNumberInput input,
.stDateInput input,
.stSelectbox [data-baseweb="select"] > div {
    background: rgba(255, 255, 255, 0.045) !important;
    color: var(--text-primary) !important;
    -webkit-text-fill-color: var(--text-primary) !important;
    border: 1px solid rgba(255, 255, 255, 0.13) !important;
    border-radius: 14px !important;
    min-height: 3.1rem !important;
    box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.03) !important;
}

.stTextInput input,
.stTextArea textarea,
.stNumberInput input,
.stDateInput input {
    padding: 0.85rem 0.95rem !important;
}

.stTextInput input::placeholder,
.stTextArea textarea::placeholder {
    color: var(--text-muted) !important;
}

.stTextInput input:focus,
.stTextArea textarea:focus,
.stNumberInput input:focus,
.stDateInput input:focus {
    border-color: rgba(74, 222, 128, 0.55) !important;
    box-shadow: 0 0 0 3px rgba(74, 222, 128, 0.12) !important;
}

.stSelectbox [data-baseweb="select"] > div:hover,
.stTextInput input:hover {
    border-color: rgba(110, 231, 140, 0.28) !important;
}

.stSelectbox svg,
.stMultiSelect svg {
    fill: var(--text-secondary) !important;
}

div[data-baseweb="popover"] ul,
div[data-baseweb="select"] ul,
div[role="listbox"] {
    background: #0f1711 !important;
    color: var(--text-primary) !important;
    border: 1px solid rgba(255, 255, 255, 0.08) !important;
}

div[role="option"] {
    color: var(--text-primary) !important;
    background: transparent !important;
}

div[role="option"][aria-selected="true"] {
    background: rgba(74, 222, 128, 0.12) !important;
    color: var(--text-primary) !important;
}

button,
button span,
[role="button"],
[role="button"] span,
.stButton button p,
.stButton button div,
.stButton button span,
.stSelectbox div,
.stTextInput input,
.stTextArea textarea,
.stMarkdown,
[data-testid="stMarkdownContainer"] * {
    opacity: 1 !important;
}

button:hover,
[role="button"]:hover,
.stButton button:hover,
.stButton button:hover span,
.stButton button:hover p {
    opacity: 1 !important;
}

.stProgress > div > div {
    background-color: rgba(255, 255, 255, 0.06) !important;
}

.stProgress > div > div > div {
    background: linear-gradient(90deg, var(--accent), var(--accent-strong)) !important;
}

.stAlert {
    background: rgba(16, 23, 18, 0.96) !important;
    border: 1px solid var(--border) !important;
    border-radius: 14px !important;
}

.stSuccess {
    border-color: rgba(74, 222, 128, 0.26) !important;
}

.stWarning {
    border-color: rgba(251, 191, 36, 0.28) !important;
}

.stInfo {
    border-color: rgba(96, 165, 250, 0.28) !important;
}

.stError {
    border-color: rgba(248, 113, 113, 0.30) !important;
}

.section-title {
    font-family: 'Space Grotesk', sans-serif !important;
    font-size: 1.15rem;
    font-weight: 700;
    color: var(--text-primary);
    margin: 1.7rem 0 0.9rem 0;
    display: flex;
    align-items: center;
    gap: 0.55rem;
}

hr {
    border: none !important;
    border-top: 1px solid rgba(255, 255, 255, 0.08) !important;
    margin: 1.8rem 0 !important;
}

@media (max-width: 900px) {
    .block-container {
        padding-top: 1.4rem !important;
    }

    .hero-banner,
    .progress-hero,
    .quiz-wrapper,
    .completion-card,
    .revise-card {
        padding: 1.25rem !important;
    }
}
</style>
"""
