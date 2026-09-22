import streamlit as st
import pandas as pd

st.title("📊 Working with CSV Files Using Pandas")

st.write("Upload a CSV file to load, view, and analyze the data.")

# 1. DATA LOADING
st.header("📂 Data Loading")

uploaded_file = st.file_uploader(
    "Upload a CSV file",
    type=["csv"]
)

if uploaded_file is not None:

    # Read CSV using Pandas
    df = pd.read_csv(uploaded_file)

    st.success("✅ CSV file loaded successfully!")

    # 2. VISUALIZATION
    st.header("📋 Dataset")

    st.dataframe(
        df,
        use_container_width=True
    )

    # 3. OPERATIONS
    st.header("⚙️ Operations")

    operation = st.selectbox(
        "Choose an operation:",
        ["Select Operation", "Filter Data", "Calculate Average"]
    )

    # Filter Data
    if operation == "Filter Data":

        column = st.selectbox(
            "Select a column to filter:",
            df.columns
        )

        value = st.text_input(
            "Enter a value to search:"
        )

        if st.button("Apply Filter"):

            filtered_data = df[
                df[column].astype(str).str.contains(
                    value,
                    case=False,
                    na=False
                )
            ]

            st.write("### Filtered Data")

            st.dataframe(
                filtered_data,
                use_container_width=True
            )

    # Calculate Average
    elif operation == "Calculate Average":

        numeric_columns = df.select_dtypes(
            include="number"
        ).columns

        if len(numeric_columns) > 0:

            column = st.selectbox(
                "Select a numeric column:",
                numeric_columns
            )

            if st.button("Calculate Average"):

                average = df[column].mean()

                st.success(
                    f"Average of {column}: {average:.2f}"
                )

        else:

            st.warning(
                "⚠️ No numeric columns found in the CSV file."
            )