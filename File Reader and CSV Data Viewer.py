import streamlit as st
import pandas as pd

st.title("📁 File Reader and CSV Data Viewer")

st.write("Upload a text file or CSV file to view its contents.")

# Create two columns
col1, col2 = st.columns(2)

# -----------------------------------
# TEXT FILE READER
# -----------------------------------

with col1:
    st.subheader("📄 Text File Reader")

    text_file = st.file_uploader(
        "Upload a TXT file",
        type=["txt"]
    )

    if text_file is not None:

        content = text_file.read().decode("utf-8")

        st.write("### File Contents")

        st.text_area(
            "Text File",
            content,
            height=300
        )


# -----------------------------------
# CSV DATA VIEWER
# -----------------------------------

with col2:
    st.subheader("📊 CSV Data Viewer")

    csv_file = st.file_uploader(
        "Upload a CSV file",
        type=["csv"]
    )

    if csv_file is not None:

        data = pd.read_csv(csv_file)

        st.write("### CSV Data")

        st.dataframe(
            data,
            use_container_width=True
        )