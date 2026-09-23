import streamlit as st
import pandas as pd

# Title
st.title("📊 Student Dataset Processor")

st.write("Upload a CSV file to view and process student data.")

# 1. FILE UPLOAD
uploaded_file = st.file_uploader(
    "Upload CSV File",
    type=["csv"]
)

if uploaded_file is not None:

    # Read CSV file
    df = pd.read_csv(uploaded_file)

    st.success("✅ CSV file uploaded successfully!")

    # 2. DATA DISPLAY
    st.header("📋 Complete Dataset")

    st.dataframe(
        df,
        use_container_width=True
    )

    # 3. DATA PROCESSING
    st.header("🔍 Data Processing")

    st.write("Showing students who scored 80 or above.")

    # Filter students with marks >= 80
    filtered_data = df[df["Marks"] >= 80]

    # 4. OUTPUT
    st.subheader("🏆 Students Scoring 80 and Above")

    st.dataframe(
        filtered_data,
        use_container_width=True
    )

    # Display number of students
    st.info(
        f"Total students scoring 80 or above: {len(filtered_data)}"
    )