import streamlit as st
import re
import requests

WEBHOOK_URL = "https://your-webhook-url.com"  # Replace with  actual webhook

def valid_email(email):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

def contact_form():
    with st.form("contact_form"):
        name = st.text_input("YOUR Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your Message")
        submit_button = st.form_submit_button("Submit")

    if submit_button:
        if not WEBHOOK_URL:
            st.error("Email service is not set up. Please try again later.", icon="📧")
            st.stop()

        if not name:
            st.error("Please provide your name.", icon="🧑")
            st.stop()

        if not email:
            st.error("Please provide your email address.", icon="📨")
            st.stop()

        if not valid_email(email):
            st.error("Please provide a valid email address.", icon="📫")
            st.stop()

        if not message:
            st.error("Please provide a message.", icon="💬")
            st.stop()

        # All validations passed: send data
        data = {
            "email": email,
            "name": name,
            "message": message
        }

        try:
            response = requests.post(WEBHOOK_URL, json=data)
            if response.status_code == 200:
                st.success("Message sent successfully!")
            else:
                st.error("Failed to send message. Please try again later.")
        except Exception as e:
            st.error(f"An error occurred: {e}")
