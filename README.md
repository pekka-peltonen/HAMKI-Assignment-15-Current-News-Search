HAMKI Assignment #15 – Current News Search and Summary

Author: Pekka Peltonen
Course: AI APIs and Standalone AI Applications

Description

A Streamlit application that searches for current news and generates summaries using the OpenAI API.

Features

Search news by topic

Select a time period: last 24 hours, 7 days or 30 days

Summarize news with source links

Separate reported facts from AI interpretation

Display error messages if an API request fails

Technologies

Python

Streamlit

OpenAI API

Model: gpt-5.6

Web search tool

How to run

Install the required packages:

python -m pip install streamlit openai

Set your OpenAI API key in the environment.

Start the application:

python -m streamlit run app.py

Open the local address displayed in the terminal.

Testing

The application was tested with the topic "Artificial intelligence" and the time period "Last 7 days".

The application successfully displayed a news summary with source links, reported facts and interpretations.

Files

app.py – application source code

Assignment_15_screenshot_1.png.png – screenshot of the application

README.md – project documentation
