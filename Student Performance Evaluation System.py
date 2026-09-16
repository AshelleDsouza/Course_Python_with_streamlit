import streamlit as st

# Task Name
st.title("🎓 Student Performance Evaluation System")

st.write("Enter the student details and evaluate the performance.")

# 1. Input Data
name = st.text_input("Enter Student Name:")

marks = st.number_input(
    "Enter Marks (0-100):",
    min_value=0,
    max_value=100,
    value=0
)

# 2. Choose Type
evaluation_type = st.selectbox(
    "Choose Evaluation Type:",
    ["Pass/Fail", "Grade", "Performance Level"]
)

# 3. Check Result
if st.button("Check Result"):

    if name == "":
        st.warning("Please enter the student's name.")

    else:

        # Pass/Fail Evaluation
        if evaluation_type == "Pass/Fail":

            if marks >= 50:
                st.success(f"🎉 {name} has Passed!")
            else:
                st.error(f"❌ {name} has Failed.")

        # Grade Evaluation
        elif evaluation_type == "Grade":

            if marks >= 90:
                st.success(f"🏆 {name}'s Grade: A+")
            elif marks >= 80:
                st.success(f"🌟 {name}'s Grade: A")
            elif marks >= 70:
                st.success(f"👍 {name}'s Grade: B")
            elif marks >= 60:
                st.info(f"📘 {name}'s Grade: C")
            elif marks >= 50:
                st.warning(f"📗 {name}'s Grade: D")
            else:
                st.error(f"❌ {name}'s Grade: F")

        # Performance Level
        elif evaluation_type == "Performance Level":

            if marks >= 80:
                st.success(f"⭐ {name} has Excellent Performance!")
            elif marks >= 60:
                st.info(f"👍 {name} has Good Performance!")
            elif marks >= 50:
                st.warning(f"📚 {name} has Average Performance.")
            else:
                st.error(f"❌ {name} needs Improvement.")