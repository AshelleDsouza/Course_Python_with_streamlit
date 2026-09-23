import streamlit as st
import json

st.title("📂 Working with JSON Data")

st.write("Upload a JSON file to read, display, and extract values.")

# 1. READ JSON
st.header("📖 Read JSON")

uploaded_file = st.file_uploader(
    "Upload a JSON file",
    type=["json"]
)

if uploaded_file is not None:

    # Read JSON file
    data = json.load(uploaded_file)

    st.success("✅ JSON file loaded successfully!")

    # 2. DISPLAY DATA
    st.header("👀 Display Data")

    st.json(data)

    # 3. EXTRACT VALUES
    st.header("🔍 Extract Values")

    if isinstance(data, dict):

        key = st.selectbox(
            "Select a key:",
            list(data.keys())
        )

        if st.button("Extract Value"):

            value = data[key]

            st.success(
                f"Value of '{key}': {value}"
            )

    else:

        st.info(
            "The uploaded JSON contains a list instead of key-value pairs."
        )