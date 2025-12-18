import streamlit as st
import pandas as pd
from joblib import load
import plotly.graph_objects as go
from datetime import date, timedelta
import io


# ----------------------------
# Page config
# ----------------------------
st.set_page_config(
    page_title="StudyBuddy — Student Performance",
    page_icon="🎓",
    layout="wide"
)


# ----------------------------
# Theme: skin background + ALL text deep purple
# ----------------------------
PURPLE = "#2A1459"     # main text (deep purple)
PURPLE_ACCENT = "#5B21B6"
MINT = "#22D3EE"
AMBER = "#FBBF24"
PINK = "#FB7185"


st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;700;800&display=swap');
html, body, [class*="css"] {{ font-family: 'Outfit', sans-serif; }}


/* Force all text dark purple */
html, body, p, li, span, div, label, small {{ color: {PURPLE} !important; }}
h1, h2, h3, h4 {{ color: {PURPLE} !important; font-weight: 900 !important; }}


.stApp {{
  background:
    radial-gradient(circle at 18% 10%, rgba(167, 139, 250, 0.22) 0%, rgba(0,0,0,0) 40%),
    radial-gradient(circle at 86% 24%, rgba(34, 211, 238, 0.18) 0%, rgba(0,0,0,0) 45%),
    radial-gradient(circle at 28% 88%, rgba(251, 191, 36, 0.18) 0%, rgba(0,0,0,0) 48%),
    linear-gradient(135deg, #FFF1E6 0%, #FCE8DD 40%, #FBE7E1 100%);
}}


.block-container {{ max-width: 1200px; padding-top: 1.6rem; }}
[data-testid="stHeader"] {{ background: transparent; }}
header {{ background: transparent; }}


/* Hero */
.hero {{
  position: relative;
  border-radius: 26px;
  padding: 22px 24px;
  background: linear-gradient(135deg, rgba(167,139,250,0.30) 0%, rgba(255,255,255,0.84) 45%, rgba(34,211,238,0.22) 100%);
  border: 1px solid rgba(88, 28, 135, 0.14);
  box-shadow: 0 18px 45px rgba(0,0,0,0.10);
  overflow: hidden;
  margin-bottom: 18px;
}}
.bubble {{ position:absolute; border-radius:999px; opacity: 0.95; }}
.b1 {{ width:190px; height:190px; right:-70px; top:-80px; background: rgba(167,139,250,0.36); }}
.b2 {{ width:150px; height:150px; left:-55px; bottom:-70px; background: rgba(34,211,238,0.28); }}
.b3 {{ width:95px; height:95px; right:120px; bottom:-35px; background: rgba(251,191,36,0.28); }}


.hero-title {{ font-size: 2.1rem; font-weight: 900; color: {PURPLE} !important; }}
.hero-sub {{ margin-top: 6px; color: rgba(42,20,89,0.78) !important; font-size: 1.0rem; line-height: 1.55; }}


.badges {{ display:flex; gap:10px; flex-wrap:wrap; margin-top: 12px; }}
.badge {{
  padding: 7px 12px; border-radius: 999px; font-size: 0.85rem; font-weight: 900;
  border: 1px solid rgba(76,29,149,0.14);
  background: rgba(255,255,255,0.85);
  color: {PURPLE} !important;
}}


/* Cards */
.card {{
  border-radius: 22px;
  background: rgba(255,255,255,0.86);
  border: 1px solid rgba(76,29,149,0.12);
  box-shadow: 0 14px 35px rgba(0,0,0,0.08);
  padding: 18px 18px;
  margin-bottom: 16px;
}}
.card-title {{
  font-weight: 900;
  letter-spacing: 0.03em;
  color: {PURPLE} !important;
  font-size: 1.05rem;
  margin-bottom: 8px;
}}
.card-sub {{
  color: rgba(42,20,89,0.78) !important;
  font-size: 0.92rem;
  line-height: 1.55;
  margin-bottom: 10px;
}}
.strip {{ height: 4px; border-radius: 999px; margin: 8px 0 12px 0; }}
.strip.p {{ background: linear-gradient(90deg, #A78BFA 0%, rgba(167,139,250,0.0) 90%); }}
.strip.c {{ background: linear-gradient(90deg, {MINT} 0%, rgba(34,211,238,0.0) 90%); }}
.strip.a {{ background: linear-gradient(90deg, {AMBER} 0%, rgba(251,191,36,0.0) 90%); }}


/* WHITE RESULT BOX */
.result-box {{
  background: white;
  border-radius: 20px;
  padding: 24px;
  margin: 20px 0;
  box-shadow: 0 8px 24px rgba(0,0,0,0.08);
  border: 1px solid rgba(76,29,149,0.08);
}}


/* Inputs - CHANGE BLACK TO PURPLE */
.stSelectbox div[data-baseweb="select"] > div,
.stTextInput input,
.stNumberInput input {{
  background: rgba(255,255,255,0.96) !important;
  border: 1px solid rgba(76,29,149,0.22) !important;
  border-radius: 14px !important;
  color: {PURPLE} !important;
}}
.stSelectbox span {{ color: {PURPLE} !important; font-weight: 800; }}


/* Fix segmented control colors - NO BLACK */
[data-baseweb="segmented-control"] {{
  background: rgba(255,255,255,0.9) !important;
  border: 1px solid rgba(167,139,250,0.3) !important;
  border-radius: 14px !important;
  padding: 4px !important;
}}
[data-baseweb="segmented-control"] button {{
  color: {PURPLE} !important;
  font-weight: 700 !important;
  border-radius: 10px !important;
  background: transparent !important;
  border: none !important;
}}
[data-baseweb="segmented-control"] button[aria-pressed="true"] {{
  background: linear-gradient(135deg, {PURPLE_ACCENT} 0%, #A78BFA 100%) !important;
  color: white !important;
}}
[data-baseweb="segmented-control"] button:hover {{
  background: rgba(167,139,250,0.15) !important;
}}


/* Number input controls - NO BLACK */
.stNumberInput button {{
  background: {PURPLE_ACCENT} !important;
  color: white !important;
  border: none !important;
  border-radius: 8px !important;
  font-weight: 900 !important;
}}
.stNumberInput button:hover {{
  background: {PURPLE} !important;
}}


/* Buttons */
.stButton > button {{
  border:none; border-radius:999px; padding:0.88rem 1.2rem;
  font-weight: 900; letter-spacing: 0.04em; color:white !important;
  background: linear-gradient(135deg, {PURPLE_ACCENT} 0%, #A78BFA 55%, {MINT} 100%);
  box-shadow: 0 16px 40px rgba(109,40,217,0.22);
}}
.stButton > button:hover {{ filter: brightness(1.03); transform: translateY(-1px); }}


/* Sidebar: about only */
[data-testid="stSidebar"] {{
  background: rgba(255,255,255,0.76);
  border-right: 1px solid rgba(76,29,149,0.12);
}}


/* Routine table styling */
.routine-table {{
  background: white;
  border-radius: 16px;
  padding: 16px;
  margin: 12px 0;
  border: 2px solid rgba(167,139,250,0.3);
}}
.time-morning {{ 
  background: linear-gradient(135deg, rgba(251,191,36,0.2), rgba(251,191,36,0.05));
  padding: 8px 12px;
  border-radius: 8px;
  border-left: 3px solid {AMBER};
  margin: 4px 0;
}}
.time-afternoon {{ 
  background: linear-gradient(135deg, rgba(34,211,238,0.2), rgba(34,211,238,0.05));
  padding: 8px 12px;
  border-radius: 8px;
  border-left: 3px solid {MINT};
  margin: 4px 0;
}}
.time-evening {{ 
  background: linear-gradient(135deg, rgba(167,139,250,0.2), rgba(167,139,250,0.05));
  padding: 8px 12px;
  border-radius: 8px;
  border-left: 3px solid {PURPLE_ACCENT};
  margin: 4px 0;
}}
</style>
""", unsafe_allow_html=True)


# ----------------------------
# Load model
# ----------------------------
@st.cache_resource
def load_model():
    return load("student_performance_knn.joblib")


model = load_model()


# ----------------------------
# Importance (hard-coded)
# ----------------------------
TOP_IMPORTANCES = {
    "study_hours": 9.410313,
    "class_attendance": 2.136929,
    "sleep_quality": 1.019855,
    "study_method": 0.697072,
    "facility_rating": 0.672568,
    "sleep_hours": 0.426760,
}


# ----------------------------
# Sidebar (About only)
# ----------------------------
with st.sidebar:
    st.markdown("### About this app")
    st.write("Model: scikit-learn Pipeline (preprocessing + KNN regressor).")
    st.write("Predicts exam score from study routine + lifestyle.")
    st.caption("Built by Mayank Goyal · 2025")


# ----------------------------
# Helpers
# ----------------------------
def chip(label, options, default, key, help=None):
    val = st.segmented_control(
        label=label,
        options=options,
        default=default,
        selection_mode="single",
        key=key,
        help=help
    )
    return val if val is not None else default


def make_plan(time_per_day: str, prep_style: str, score: float | None, sleep_quality: str, attendance: float):
    """Return a 7-day plan with MORNING/AFTERNOON/EVENING breakdown."""
    minutes_map = {"1h": 60, "2h": 120, "3h": 180, "4+h": 240}
    minutes = minutes_map.get(time_per_day, 120)


    # Choose focus distribution
    if prep_style == "Board (theory)":
        focus = {"Concepts/Notes": 0.45, "Revision": 0.30, "Practice": 0.25}
    else:  # Practical/MCQ
        focus = {"Concepts/Notes": 0.30, "Revision": 0.20, "Practice": 0.50}


    # Adjust using prediction signals
    if score is not None and score < 60:
        focus = {"Concepts/Notes": focus["Concepts/Notes"] + 0.10,
                 "Revision": focus["Revision"] + 0.10,
                 "Practice": max(0.15, focus["Practice"] - 0.20)}


    # Build plan with time-of-day breakdown
    start = date.today()
    rows = []
    for d in range(7):
        day = start + timedelta(days=d)


        concept_m = int(minutes * focus["Concepts/Notes"])
        revise_m = int(minutes * focus["Revision"])
        practice_m = minutes - concept_m - revise_m


        # Distribute across morning, afternoon, evening
        # Morning: 40% (fresh mind - concepts/theory)
        # Afternoon: 35% (practice)
        # Evening: 25% (revision)
        morning_min = int(minutes * 0.40)
        afternoon_min = int(minutes * 0.35)
        evening_min = minutes - morning_min - afternoon_min


        # Assign activities by time of day
        if prep_style == "Board (theory)":
            morning_activity = f"Concepts/Notes ({morning_min} min)"
            afternoon_activity = f"Revision ({afternoon_min} min)"
            evening_activity = f"Practice + Quick recap ({evening_min} min)"
        else:
            morning_activity = f"Concepts ({morning_min} min)"
            afternoon_activity = f"Practice/MCQs ({afternoon_min} min)"
            evening_activity = f"Revision + PYQs ({evening_min} min)"


        # Wellbeing suggestions
        if sleep_quality == "poor":
            wellbeing = "Sleep fix: no screens 45 min before bed"
        else:
            wellbeing = "10–15 min walk + hydrate"


        # Attendance booster
        if attendance < 60:
            extra = "Catch-up: 20 min class notes (replace evening activity)"
        else:
            extra = "Maintain ≥75% attendance this week"


        rows.append({
            "Day": day.strftime("%a, %d %b"),
            "🌅 Morning": morning_activity,
            "☀️ Afternoon": afternoon_activity,
            "🌙 Evening": evening_activity,
            "💡 Extra Focus": extra,
            "🧘 Wellbeing": wellbeing
        })


    return pd.DataFrame(rows)


def df_to_csv_bytes(df: pd.DataFrame) -> bytes:
    return df.to_csv(index=False).encode("utf-8")


# ----------------------------
# HERO
# ----------------------------
st.markdown(f"""
<div class="hero">
  <div class="bubble b1"></div>
  <div class="bubble b2"></div>
  <div class="bubble b3"></div>


  <div class="hero-title"><b>🎓 StudyBuddy</b> — Student Performance Predictor</div>
  <div class="hero-sub">
    Predict your exam score, view clean insights, and generate a realistic 7‑day routine — all in one place.
  </div>


  <div class="badges">
    <div class="badge">No sliders ✅</div>
    <div class="badge">Premium charts</div>
    <div class="badge">7‑Day plan inside app</div>
  </div>
</div>
""", unsafe_allow_html=True)


# ----------------------------
# INPUTS (NO sliders)
# ----------------------------
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown('<div class="card-title">✍️ Student Profile</div>', unsafe_allow_html=True)
st.markdown('<div class="strip p"></div>', unsafe_allow_html=True)
st.markdown('<div class="card-sub">Use steppers + chips (fast, clean, mobile-friendly).</div>', unsafe_allow_html=True)


c1, c2 = st.columns(2)
with c1:
    age = st.number_input("Age", min_value=17, max_value=30, value=20, step=1)
    study_hours = st.number_input("Daily study hours", min_value=0.0, max_value=12.0, value=4.0, step=0.25, format="%.2f")
    class_attendance = st.number_input("Attendance (%)", min_value=0.0, max_value=100.0, value=75.0, step=1.0, format="%.0f")
    sleep_hours = st.number_input("Sleep hours (night)", min_value=3.0, max_value=12.0, value=7.0, step=0.25, format="%.2f")


with c2:
    gender = chip("Gender", ["male", "female", "other"], default="male", key="gender_chip")
    internet_access = chip("Internet access", ["yes", "no"], default="yes", key="net_chip")
    sleep_quality = chip("Sleep quality", ["poor", "average", "good"], default="average", key="sleepq_chip")
    exam_difficulty = chip("Exam difficulty", ["easy", "moderate", "hard"], default="moderate", key="diff_chip")


course = chip("Course", ["bca", "bba", "ba", "b.sc", "diploma", "other"], default="bca", key="course_chip")
study_method = chip("Study method", ["self-study", "group study", "coaching", "online videos"], default="self-study", key="method_chip")
facility_rating = chip("Facility rating", ["low", "medium", "high"], default="medium", key="facility_chip")


st.markdown("</div>", unsafe_allow_html=True)


input_df = pd.DataFrame([{
    "age": age,
    "gender": gender,
    "course": course,
    "study_hours": study_hours,
    "class_attendance": class_attendance,
    "internet_access": internet_access,
    "sleep_hours": sleep_hours,
    "sleep_quality": sleep_quality,
    "study_method": study_method,
    "facility_rating": facility_rating,
    "exam_difficulty": exam_difficulty
}])


with st.expander("👀 Preview input"):
    st.dataframe(input_df, use_container_width=True)


# ----------------------------
# PREDICTION (WHITE ROUNDED BOX)
# ----------------------------
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown('<div class="card-title">📌 Prediction</div>', unsafe_allow_html=True)
st.markdown('<div class="strip c"></div>', unsafe_allow_html=True)
st.markdown('<div class="card-sub">Predict score + get a dial + quick improvement tips.</div>', unsafe_allow_html=True)


if "last_score" not in st.session_state:
    st.session_state.last_score = None


predict_btn = st.button("🚀 Predict my exam score")


if predict_btn:
    pred = float(model.predict(input_df)[0])
    st.session_state.last_score = max(0.0, min(100.0, pred))


score = st.session_state.last_score


if score is not None:
    band = "Excellent" if score >= 85 else "Good" if score >= 70 else "Needs Work" if score >= 50 else "At Risk"
    band_color = "#16a34a" if band == "Excellent" else "#2563eb" if band == "Good" else "#f59e0b" if band == "Needs Work" else "#ef4444"


    # WHITE RESULT BOX
    st.markdown('<div class="result-box">', unsafe_allow_html=True)

    m1, m2, m3 = st.columns(3)
    with m1:
        st.metric("Estimated score", f"{score:.1f} / 100")
    with m2:
        st.metric("Band", band)
    with m3:
        st.metric("Difficulty", exam_difficulty)


    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=score,
        number={"suffix": " / 100", "font": {"size": 36, "color": PURPLE}},
        gauge={
            "axis": {"range": [0, 100]},
            "bar": {"color": PURPLE_ACCENT},
            "bgcolor": "rgba(255,255,255,0.0)",
            "steps": [
                {"range": [0, 50], "color": "rgba(239, 68, 68, 0.18)"},
                {"range": [50, 70], "color": "rgba(245, 158, 11, 0.18)"},
                {"range": [70, 85], "color": "rgba(37, 99, 235, 0.16)"},
                {"range": [85, 100], "color": "rgba(22, 163, 74, 0.16)"},
            ],
            "threshold": {"line": {"color": band_color, "width": 6}, "thickness": 0.85, "value": score},
        },
        title={"text": f"<b style='color:{PURPLE}'>Predicted Score Dial</b><br><span style='color:{PURPLE}'>Band: {band}</span>"}
    ))
    fig.update_layout(
        height=320,
        margin=dict(l=10, r=10, t=70, b=10),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)"
    )
    st.plotly_chart(fig, use_container_width=True)

    st.markdown('</div>', unsafe_allow_html=True)


    st.markdown("#### Smart tips")
    tips = []
    if study_hours < 2:
        tips.append("Study time is low — target +60–90 mins/day.")
    if class_attendance < 60:
        tips.append("Attendance is low — aim ≥ 75% to stabilize performance.")
    if sleep_quality == "poor":
        tips.append("Sleep quality is poor — fix sleep schedule, reduce late-night screen time.")
    if exam_difficulty == "hard":
        tips.append("Hard exam — add timed practice + PYQs this week.")
    if not tips:
        st.success("Routine looks balanced. Keep consistency + do timed practice. ✅")
    else:
        for t in tips:
            st.info(t)


st.markdown("</div>", unsafe_allow_html=True)


# ----------------------------
# INSIGHTS (Plotly bar)
# ----------------------------
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown('<div class="card-title">🧠 Insights</div>', unsafe_allow_html=True)
st.markdown('<div class="strip a"></div>', unsafe_allow_html=True)
st.markdown('<div class="card-sub">Feature impact from permutation importance (dashboard style).</div>', unsafe_allow_html=True)


imp_df = (
    pd.DataFrame({"feature": list(TOP_IMPORTANCES.keys()), "importance": list(TOP_IMPORTANCES.values())})
    .sort_values("importance", ascending=True)
)


colors = []
for f in imp_df["feature"]:
    if f == "study_hours":
        colors.append(PURPLE_ACCENT)
    elif f == "class_attendance":
        colors.append(MINT)
    elif f == "sleep_quality":
        colors.append(AMBER)
    else:
        colors.append(PINK)


fig_imp = go.Figure(go.Bar(
    y=imp_df["feature"],
    x=imp_df["importance"],
    orientation="h",
    marker=dict(color=colors),
    hovertemplate="<b>%{y}</b><br>importance: %{x:.3f}<extra></extra>",
))
fig_imp.update_layout(
    height=330,
    margin=dict(l=20, r=20, t=10, b=20),
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=dict(showgrid=True, gridcolor="rgba(42,20,89,0.12)", zeroline=False, title="Importance"),
    yaxis=dict(showgrid=False, title=""),
    font=dict(color=PURPLE),
)
try:
    fig_imp.update_layout(barcornerradius=14)
except Exception:
    pass


st.plotly_chart(fig_imp, use_container_width=True)
st.markdown("</div>", unsafe_allow_html=True)


# ----------------------------
# 7‑DAY ROUTINE GENERATOR (WITH TIME-OF-DAY)
# ----------------------------
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown('<div class="card-title">🗓️ 7‑Day Routine Generator</div>', unsafe_allow_html=True)
st.markdown('<div class="strip p"></div>', unsafe_allow_html=True)
st.markdown('<div class="card-sub">Choose your available time + exam style → generate a realistic plan with morning/afternoon/evening breakdown.</div>', unsafe_allow_html=True)


time_per_day = chip(
    "How much time can you study per day (next 7 days)?",
    ["1h", "2h", "3h", "4+h"],
    default="2h",
    key="plan_time"
)
prep_style = chip(
    "Prep style",
    ["Board (theory)", "Practical/MCQ"],
    default="Practical/MCQ",
    key="plan_style"
)


st.markdown("<div class='card-sub'><b>Pro tip:</b> Generate after predicting score for best personalization.</div>", unsafe_allow_html=True)


if "routine_df" not in st.session_state:
    st.session_state.routine_df = None


gen = st.button("🧩 Generate 7‑day routine")


if gen:
    st.session_state.routine_df = make_plan(
        time_per_day=time_per_day,
        prep_style=prep_style,
        score=st.session_state.last_score,
        sleep_quality=sleep_quality,
        attendance=float(class_attendance),
    )


routine_df = st.session_state.routine_df
if routine_df is not None:
    st.success("7‑day routine generated with time-of-day breakdown ✅")

    # Display with styled time blocks
    st.markdown('<div class="routine-table">', unsafe_allow_html=True)
    for idx, row in routine_df.iterrows():
        st.markdown(f"### {row['Day']}")
        st.markdown(f'<div class="time-morning"><b>🌅 Morning:</b> {row["🌅 Morning"]}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="time-afternoon"><b>☀️ Afternoon:</b> {row["☀️ Afternoon"]}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="time-evening"><b>🌙 Evening:</b> {row["🌙 Evening"]}</div>', unsafe_allow_html=True)
        st.markdown(f"**💡 Extra Focus:** {row['💡 Extra Focus']}")
        st.markdown(f"**🧘 Wellbeing:** {row['🧘 Wellbeing']}")
        if idx < len(routine_df) - 1:
            st.markdown("---")
    st.markdown('</div>', unsafe_allow_html=True)


    csv_bytes = df_to_csv_bytes(routine_df)
    st.download_button(
        label="⬇️ Download routine as CSV",
        data=csv_bytes,
        file_name="studybuddy_7_day_routine.csv",
        mime="text/csv"
    )


st.markdown("</div>", unsafe_allow_html=True)


# ----------------------------
# Footer
# ----------------------------
st.markdown(f"""
<hr style="margin-top:2.2rem; border-color: rgba(76,29,149,0.20); border-width:1px;">
<div style="text-align:center; padding:1.1rem 0; font-size:0.85rem; color:{PURPLE};">
  © 2025 <span style="font-weight:900;">StudyBuddy</span> · Student Performance Prediction · Built by
  <span style="font-weight:900; color:{PURPLE_ACCENT};">Mayank Goyal</span><br>
  <a href="https://www.linkedin.com/in/mayank-goyal-4b8756363" target="_blank"
     style="color:{PURPLE}; text-decoration:none; font-weight:900; margin-right:14px;">LinkedIn</a>
  <a href="https://github.com/mayank-goyal09" target="_blank"
     style="color:{PURPLE}; text-decoration:none; font-weight:900;">GitHub</a><br>
  <span style="font-size:0.78rem;">🎓 KNN Pipeline · Plotly Gauge · Routine Planner</span>
</div>
""", unsafe_allow_html=True)
