
import re
import streamlit as st

st.set_page_config(
    page_title="InterviewReady",
    page_icon="🎯",
    layout="wide",
)

QUESTIONS = {
    "HR & Introduction": [
        {
            "question": "Tell me about yourself.",
            "hint": "Connect your education, skills, projects and career goals.",
            "keywords": ["education", "skills", "project", "goal", "experience"],
        },
        {
            "question": "What are your strengths?",
            "hint": "Describe two relevant strengths with examples.",
            "keywords": ["strength", "example", "skills", "team", "result"],
        },
        {
            "question": "Why should we hire you?",
            "hint": "Explain what you can contribute and how you are willing to learn.",
            "keywords": ["skills", "contribute", "learn", "team", "project"],
        },
    ],
    "Behavioral": [
        {
            "question": "Describe a challenge you faced and how you handled it.",
            "hint": "Use STAR: Situation, Task, Action and Result.",
            "keywords": ["situation", "task", "action", "result", "learned"],
        },
        {
            "question": "Describe a time you worked in a team.",
            "hint": "Explain your role, contribution and the outcome.",
            "keywords": ["team", "role", "communicate", "contribution", "result"],
        },
    ],
    "Technical & Projects": [
        {
            "question": "Explain a project you worked on.",
            "hint": "Describe the problem, tools, your role and the result.",
            "keywords": ["problem", "tools", "role", "challenge", "result"],
        },
        {
            "question": "How do you approach a difficult problem?",
            "hint": "Explain how you break it down, research, test and learn.",
            "keywords": ["understand", "break", "research", "test", "learn"],
        },
    ],
}


def evaluate_answer(answer, question):
    words = re.findall(r"\b[\w'-]+\b", answer)
    text = answer.lower()

    matched = [
        keyword
        for keyword in question["keywords"]
        if keyword in text
    ]

    example = any(
        phrase in text
        for phrase in [
            "for example",
            "for instance",
            "during my",
            "such as",
        ]
    )

    score = min(
        100,
        (30 if len(words) >= 40 else 15 if len(words) >= 20 else 5)
        + round(45 * len(matched) / len(question["keywords"]))
        + (25 if example else 0),
    )

    improvements = []

    if len(words) < 40:
        improvements.append(
            "Add more detail. Aim for around 40–100 words."
        )

    if not matched:
        improvements.append(
            "Address the main themes in the question."
        )

    if not example:
        improvements.append(
            "Include a specific example from your studies or projects."
        )

    return score, len(words), matched, improvements

if "attempts" not in st.session_state:
    st.session_state.attempts = []

st.title("🎯 AI Tutor for Interview Preparation")
st.write("Your interview preparation tutor for students and freshers.")

page = st.sidebar.radio(
    "Navigate",
    ["Dashboard", "Practice Questions", "My Progress", "About"],
)

if page == "Dashboard":
    attempts = st.session_state.attempts

    average = (
        round(sum(item["score"] for item in attempts) / len(attempts))
        if attempts
        else 0
    )

    first, second, third = st.columns(3)
    first.metric("Answers practised", len(attempts))
    second.metric("Average practice score", f"{average}/100")
    third.metric("Question categories", len(QUESTIONS))

    st.subheader("Your preparation checklist")
    st.checkbox("Prepare a short self-introduction")
    st.checkbox("Choose two projects to discuss")
    st.checkbox("Prepare a teamwork example")
    st.checkbox("Prepare questions for the interviewer")

    st.info("Select Practice Questions in the sidebar to begin.")

elif page == "Practice Questions":
    category = st.selectbox(
        "Choose a category",
        list(QUESTIONS),
    )

    question_list = QUESTIONS[category]

    selected = st.selectbox(
        "Choose an interview question",
        question_list,
        format_func=lambda item: item["question"],
    )

    st.info(selected["question"])
    st.caption("Hint: " + selected["hint"])

    answer = st.text_area(
        "Write your answer",
        height=180,
        placeholder="Write your answer here. Include a real example if possible.",
    )

    if st.button("Evaluate my answer", type="primary"):
        if not answer.strip():
            st.warning("Please write an answer first.")
        else:
            score, word_count, matched, improvements = evaluate_answer(
                answer,
                selected,
            )

            st.session_state.attempts.append({
                "question": selected["question"],
                "category": category,
                "score": score,
                "words": word_count,
            })

            st.subheader("Your practice feedback")

            first, second = st.columns(2)
            first.metric("Practice score", f"{score}/100")
            second.metric("Word count", word_count)

            st.caption(
                "This is a simple rule-based practice score, "
                "not an AI assessment of your actual interview ability."
            )

            if matched:
                st.write(
                    "**Relevant themes found:** " + ", ".join(matched)
                )
            else:
                st.write(
                    "**Relevant themes:** None of the suggested keywords found."
                )

            st.write("**Suggestions to improve**")

            if improvements:
                for suggestion in improvements:
                    st.write("- " + suggestion)
            else:
                st.success(
                    "Good practice response. Keep refining your examples!"
                )

elif page == "My Progress":
    attempts = st.session_state.attempts

    if not attempts:
        st.info(
            "Your practice history will appear here after your first answer."
        )
    else:
        st.metric("Completed answers", len(attempts))

        st.dataframe(
            attempts,
            use_container_width=True,
            hide_index=True,
        )

        csv_text = "Question,Category,Score,Words\n" + "\n".join(
            '"' + item["question"].replace('"', '""') + '",'
            '"' + item["category"].replace('"', '""') + '",'
            + str(item["score"]) + ","
            + str(item["words"])
            for item in attempts
        )

        st.download_button(
            "Download progress as CSV",
            data=csv_text,
            file_name="interview_progress.csv",
            mime="text/csv",
        )

else:
    st.subheader("About InterviewReady")

    st.write(
        "InterviewReady helps students and freshers practise common "
        "HR, behavioral and technical interview questions."
    )

    st.write(
        "Current features: question bank, answer feedback and practice history."
    )

    st.warning(
        "Feedback currently uses simple rules and keywords. It is not "
        "powered by a live AI model, and progress lasts only for the current "
        "session."
    )

st.divider()
st.caption("InterviewReady | Practise thoughtfully. Grow confidently.")
