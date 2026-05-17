import streamlit as st

# Page settings
st.set_page_config(
    page_title="Course Approval Bot",
    page_icon="🎓",
    layout="centered"
)

# Title
st.title("🎓 Course Approval Bot")

st.write("""
Welcome!

This system helps students check whether courses
from their previous major can be approved
after switching majors.
""")

st.divider()

# Inputs
old_major = st.text_input("📚 Previous Major")

old_course = st.text_input("📖 Completed Course")

new_major = st.text_input("🎯 New Major")

# Button
if st.button("Check Approval"):

    approved_courses = [
        "microeconomics",
        "statistics",
        "research methods",
        "accounting basics"
    ]

    if old_course.lower() in approved_courses:

        st.success("✅ This course is likely to be approved!")

        st.info("You may not need to retake this course.")

    else:

        st.warning("⚠️ No automatic approval found.")

        st.write("We recommend sending a request to the administration.")

        email_text = f"""
Hello,

I recently switched from {old_major} to {new_major}.

I already completed the course:
{old_course}

I would like to request approval for this course in my new program.

Thank you.
"""

        st.text_area(
            "📩 Generated Request",
            email_text,
            height=220
        )

st.divider()

st.caption("🚀 MVP Prototype - Vibe Coding Course")
