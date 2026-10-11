import streamlit as st
from openai import OpenAI
import openai
st.title("Current News Search and Summary")
st.write("HAMKI Assignment #15")
st.write("News search application")

st.subheader("Search settings")

topic = st.text_input(
    "News topic",
    placeholder="e.g. Artificial intelligence"
)

period = st.selectbox(
    "Time period",
    ["Last 24 hours", "Last 7 days", "Last 30 days"]
)

search_button = st.button("Search news")

if search_button:
    if not topic.strip():
        st.warning("Please enter a news topic.")
    else:
        try:   
            client = OpenAI()

            with st.spinner("Searching current news..."):
                response = client.responses.create(
                model="gpt-5.6",
                tools=[{"type": "web_search"}],
                input=(
                    f"Find important news about {topic} "
                    f"from the period: {period}. "
                    "Summarize the findings, include source links, "
                    "and clearly separate reported facts "
                    "from your own interpretation. "
                    "If no relevant news is found, say so. "
                    "Use at most five sources."
                )
            )

            st.write(response.output_text)

        except openai.APIError as error:
            st.error(f"News search failed: {error}")
