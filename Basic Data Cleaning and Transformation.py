import streamlit as st
import pandas as pd

st.title("🧹 Basic Data Cleaning and Transformation")

st.write("Upload a CSV file to identify missing values and clean the data.")

# 1. LOAD DATA
st.header("📂 1. Load Data")

uploaded_file = st.file_uploader(
    "Upload a CSV file",
    type=["csv"]
)

if uploaded_file is not None:

    # Read CSV using Pandas
    df = pd.read_csv(uploaded_file)

    st.success("✅ CSV file loaded successfully!")

    st.subheader("Original Data")
    st.dataframe(df, use_container_width=True)

    # 2. IDENTIFY MISSING VALUES
    st.header("🔍 2. Identify Missing Values")

    missing_values = df.isnull().sum()

    st.write("Missing values in each column:")

    st.dataframe(missing_values)

    total_missing = missing_values.sum()

    if total_missing == 0:
        st.success("✅ No missing values found!")
    else:
        st.warning(
            f"⚠️ {total_missing} missing value(s) found."
        )

    # 3. CLEAN & TRANSFORM
    st.header("✨ 3. Clean & Transform")

    cleaning_option = st.selectbox(
        "Choose a cleaning operation:",
        [
            "Select Operation",
            "Fill Missing Values",
            "Remove Rows with Missing Values",
            "Remove Duplicate Rows"
        ]
    )

    if cleaning_option == "Fill Missing Values":

        cleaned_df = df.copy()

        # Fill numeric columns with their mean
        numeric_columns = cleaned_df.select_dtypes(
            include="number"
        ).columns

        for column in numeric_columns:
            cleaned_df[column] = cleaned_df[column].fillna(
                cleaned_df[column].mean()
            )

        # Fill text columns with "Unknown"
        text_columns = cleaned_df.select_dtypes(
            include="object"
        ).columns

        for column in text_columns:
            cleaned_df[column] = cleaned_df[column].fillna(
                "Unknown"
            )

        st.success("✅ Missing values have been filled.")

        # 4. DISPLAY RESULTS
        st.header("👀 4. Display Results")

        st.dataframe(
            cleaned_df,
            use_container_width=True
        )

    elif cleaning_option == "Remove Rows with Missing Values":

        cleaned_df = df.dropna()

        st.success("✅ Rows containing missing values were removed.")

        st.header("👀 4. Display Results")

        st.dataframe(
            cleaned_df,
            use_container_width=True
        )

    elif cleaning_option == "Remove Duplicate Rows":

        cleaned_df = df.drop_duplicates()

        st.success("✅ Duplicate rows were removed.")

        st.header("👀 4. Display Results")

        st.dataframe(
            cleaned_df,
            use_container_width=True
        )