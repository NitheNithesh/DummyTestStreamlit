import streamlit as st

st.set_page_config(
    page_title="Digital Productivity Index | Demo",
    page_icon="📊",
    layout="centered",
)

st.title("Digital Productivity Index")
st.caption("Interactive prototype • Demonstration only")

st.info(
    "This is a dummy prototype to test the Streamlit page layout and public hosting. "
    "It does not save responses, and its sample scores and recommendations are not validated research results."
)

st.markdown(
    """
    ### Explore your digital work habits
    Rate each area based on your typical working habits. In the final research app,
    these sections will use the approved questionnaire and scoring methodology.
    """
)

dimensions = [
    ("Planning & Prioritization", "How consistently do you plan and prioritize your work?"),
    ("Focus Management", "How often can you work without unnecessary interruptions?"),
    ("Notification Management", "How effectively do you manage notifications and alerts?"),
    ("Meeting Effectiveness", "How effectively do meetings support your work?"),
    ("AI Utilization", "How effectively do you use AI tools for appropriate work tasks?"),
    ("Information Management", "How easily can you organize and retrieve digital information?"),
    ("Digital Wellbeing", "How well do you maintain healthy digital work boundaries?"),
]

ratings = {}
with st.form("dpi_demo_form"):
    st.subheader("Self-assessment")
    st.write("Choose a rating from 1 (rarely) to 5 (consistently).")
    for name, question in dimensions:
        ratings[name] = st.slider(
            f"{name} — {question}",
            min_value=1,
            max_value=5,
            value=3,
            key=name,
        )
    submitted = st.form_submit_button("Calculate demo score", type="primary", use_container_width=True)

if submitted:
    scores = {name: round((rating - 1) / 4 * 100) for name, rating in ratings.items()}
    dpi = round(sum(scores.values()) / len(scores))

    st.divider()
    st.subheader("Your demo results")
    left, right = st.columns(2)
    left.metric("Demo DPI score", f"{dpi}/100")
    right.metric("Dimensions assessed", len(scores))

    if dpi >= 80:
        summary = "Your demo responses indicate consistently strong digital work habits across the areas assessed."
    elif dpi >= 60:
        summary = "Your demo responses indicate a mixed profile, with some habits that may be working well and others worth reviewing."
    else:
        summary = "Your demo responses suggest several digital work habits may be worth reviewing and strengthening."
    st.write(summary)

    st.markdown("#### Dimension scores")
    for name, score in sorted(scores.items(), key=lambda item: item[1], reverse=True):
        st.write(f"**{name}: {score}/100**")
        st.progress(score / 100)

    best = max(scores, key=scores.get)
    needs_work = min(scores, key=scores.get)
    st.markdown("#### What may be working well")
    st.write(f"**{best}** is your highest-scoring area in this demonstration. Consider keeping the routines that support it.")

    suggestions = {
        "Planning & Prioritization": "Try choosing three priority tasks at the start of each workday and reviewing them before finishing.",
        "Focus Management": "Try scheduling short focus blocks, reducing task switching, and protecting time for demanding work.",
        "Notification Management": "Review non-essential alerts and batch notifications where your role allows it.",
        "Meeting Effectiveness": "Set a clear purpose and expected outcome before meetings; share action items afterward.",
        "AI Utilization": "Identify repeatable, low-risk tasks where approved AI tools can help, and verify outputs before using them.",
        "Information Management": "Use consistent file names, folder structures, and a trusted place to capture notes and tasks.",
        "Digital Wellbeing": "Review after-hours digital work and create realistic boundaries for breaks and availability.",
    }
    st.markdown("#### An area to consider improving")
    st.write(f"**{needs_work}** is your lowest-scoring area in this demonstration.")
    st.write(suggestions[needs_work])

    st.caption(
        "Interpretation note: these scores are generated from a simple demonstration formula. "
        "The final DPI formula, interpretation bands, and recommendations must be defined and evaluated as part of the research."
    )

st.divider()
st.caption("Prototype for the proposed MBA research project. No respondent data is stored by this demo.")
