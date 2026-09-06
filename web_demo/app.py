import streamlit as st


st.title("🤖 AICraft AI Code Explainer")

st.write(
    "Upload Python code and get an AI explanation."
)


uploaded_file = st.file_uploader(
    "Upload Python file",
    type=["py"]
)


if uploaded_file:

    code = uploaded_file.read().decode(
        "utf-8"
    )

    st.subheader(
        "Your Code"
    )

    st.code(
        code,
        language="python"
    )


    st.subheader(
        "AI Explanation"
    )

    st.info(
        """
        This demo will explain your code
        using AI assistance.

        Future versions will connect
        directly with AI models.
        """
    )
