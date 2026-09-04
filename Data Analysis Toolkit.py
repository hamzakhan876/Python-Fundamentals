import streamlit as st
import pandas as pd
import plotly.express as px


# -------------------------
# Page Title
# -------------------------

st.title("Data Analysis Toolkit")


# -------------------------
# CSV Upload
# -------------------------

uploaded_file = st.file_uploader(
    "Upload your CSV file",
    type=["csv"]
)


# Only run the analysis after a file is uploaded
if uploaded_file:

    # Read CSV
    df = pd.read_csv(uploaded_file)

    st.success("CSV loaded successfully!")


    # -------------------------
    # Dataset Information
    # -------------------------

    st.subheader("Dataset Information")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Rows", df.shape[0])

    with col2:
        st.metric("Columns", df.shape[1])

    with col3:
        st.metric(
            "Missing Values",
            df.isnull().sum().sum()
        )


    # -------------------------
    # Data Preview
    # -------------------------

    st.subheader("Data Preview")

    rows = st.slider(
        "Number of rows to display",
        min_value=5,
        max_value=50,
        value=10
    )

    st.dataframe(df.head(rows))


    # -------------------------
    # Statistics
    # -------------------------

    st.subheader("Statistics")

    st.dataframe(df.describe())


    # -------------------------
    # Chart Selector
    # -------------------------

    st.subheader("Create a Chart")

    # Find numeric columns
    numeric_columns = df.select_dtypes(
        include="number"
    ).columns.tolist()


    if len(numeric_columns) >= 2:

        chart_type = st.selectbox(
            "Choose a chart",
            [
                "Bar Chart",
                "Line Chart",
                "Scatter Chart"
            ]
        )

        x_column = st.selectbox(
            "Choose X-axis",
            numeric_columns
        )

        y_column = st.selectbox(
            "Choose Y-axis",
            numeric_columns
        )


        # -------------------------
        # Create Chart
        # -------------------------

        if chart_type == "Bar Chart":

            fig = px.bar(
                df,
                x=x_column,
                y=y_column
            )

        elif chart_type == "Line Chart":

            fig = px.line(
                df,
                x=x_column,
                y=y_column
            )

        elif chart_type == "Scatter Chart":

            fig = px.scatter(
                df,
                x=x_column,
                y=y_column
            )


        # -------------------------
        # Display Chart
        # -------------------------

        st.plotly_chart(
            fig,
            use_container_width=True
        )


    else:

        st.warning(
            "The CSV needs at least two numeric columns."
        )