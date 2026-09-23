import streamlit as st
import pandas as pd

st.title("📂 CSV File Viewer")

st.write("Upload a CSV file to view its contents.")

# File Upload
uploaded_file = st.file_uploader(
    "Upload CSV File",
    type=["csv"]
)

# Display uploaded file
if uploaded_file is not None:

    # Read CSV using Pandas
    data = pd.read_csv(uploaded_file)

    st.success("✅ File uploaded successfully!")

    # Display file name
    st.write("### 📄 File Name")
    st.write(uploaded_file.name)

    # Display data
    st.write("### 📊 CSV Data")

    st.dataframe(
        data,
        use_container_width=True
    )