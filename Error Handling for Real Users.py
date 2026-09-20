import streamlit as st

st.title("🎓 Student Result Checker")

st.write("Enter your name and marks to check your result.")

# Input Data
name = st.text_input("Enter your name:")

marks = st.number_input(
    "Enter your marks (0-100):",
    min_value=0,
    max_value=100,
    value=None,
    placeholder="Enter marks"
)

# Check Result
if st.button("Check Result"):

    # Validation
    if name.strip() == "":
        st.error("❌ Please enter your name.")

    elif marks is None:
        st.error("❌ Please enter your marks.")

    # Success Case
    elif marks >= 50:
        st.success(f"✅ Congratulations {name}! You have PASSED.")

    # Fail Case
    else:
        st.warning(f"⚠️ Sorry {name}, you have FAILED.")
