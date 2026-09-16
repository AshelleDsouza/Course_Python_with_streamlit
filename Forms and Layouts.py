import streamlit as st

st.title("🎓 Student Application Form")
st.write("Complete the form to verify your result.")

# Form Submission
with st.form("student_form"):

    st.subheader("📝 Form Submission")

    name = st.text_input("Student Name")
    reg_no = st.text_input("Registration Number")
    marks = st.number_input(
        "Enter Marks",
        min_value=0,
        max_value=100,
        value=0
    )

    submitted = st.form_submit_button("Submit Application")

# Result Verification
if submitted:

    st.subheader("📊 Result Verification")

    if name == "" or reg_no == "":
        st.warning("Please fill in all the required fields.")

    elif marks >= 50:
        st.success(f"✅ Application submitted successfully!")
        st.success(f"Congratulations {name}! You have PASSED.")

    else:
        st.error(f"❌ Application submitted.")
        st.error(f"Sorry {name}, you have FAILED.")