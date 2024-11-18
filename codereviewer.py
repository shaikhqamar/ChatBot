import streamlit as st
import google.generativeai as genai
import time

# Configure the Google Generative AI API
genai.configure(api_key="PUT YOUR API KEY HERE")  # Replace with your actual API key

# Set up the app layout
st.set_page_config(page_title="AI Code Reviewer", layout="wide")

# Title and Description
st.title("👨‍💻 AI Code Reviewer")
st.write("Enter your Python code below, and let the AI identify bugs or areas for improvement. Just click the button below to get started!")

# Create a two-column layout for input and output
col1, col2 = st.columns([2, 3])

# Code input section
with col1:
    st.subheader("Step 1: Enter Your Python Code")
    user_code = st.text_area("Enter your Python code here...", height=300, help="Paste your Python code for review here.")

# Button to trigger code review
with col2:
    if st.button("Generate Code Review"):
        if user_code.strip() == "":
            st.warning("Please enter some Python code to review.")
        else:
            # Show loading spinner while AI is processing the request
            with st.spinner("Reviewing your code..."):
                try:
                    # Initialize the generative model
                    llm = genai.GenerativeModel("models/gemini-1.5-flash")

                    # Start a chat session
                    chatbot = llm.start_chat(history=[])

                    # Send the code to the model for review
                    response = chatbot.send_message(f"Review the following Python code and identify any bugs or improvements:\n{user_code}")
                    
                    # Simulate some delay for AI to process the request
                    time.sleep(2)  # Remove or adjust as necessary for your needs

                    # Display the review result
                    st.subheader("Step 2: AI Code Review")
                    st.success("Code review complete! Here's the feedback:")
                    st.markdown(f"### Bug Report / Recommendations:")
                    st.write(response.text)

                except Exception as e:
                    st.error(f"An error occurred while generating the review: {str(e)}")

# Footer section
st.markdown("""
    ---
    Made with ❤️ using [Streamlit](https://streamlit.io) and [Google Generative AI](https://cloud.google.com/generative-ai) by QAMAR.
    """)

