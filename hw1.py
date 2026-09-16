import streamlit as st

st.title("🎓 Student Performance Evaluator")

name = st.text_input("Enter your name")

marks = st.number_input(
    "Enter your marks (0-100)",
    min_value=0,
    max_value=100
)

if st.button("Evaluate Performance"):

    if marks >= 50:
        st.success(f"🎉 Congratulations {name}! You have passed.")
    else:
        st.error(f"❌ Sorry {name}, you have failed.")