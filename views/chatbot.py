import streamlit as st
import requests

# Set page title
st.title("GPT Chatbot (OpenRouter)")

# Load API key from secrets
api_key = st.secrets["OPENROUTER_API_KEY"]

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [{"role": "system", "content": "You are a helpful assistant."}]

# User input
user_input = st.text_input("You:", key="input")

# When user enters a message
if user_input:
    st.session_state.chat_history.append({"role": "user", "content": user_input})

    # Send to OpenRouter API
    try:
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json"
            },
            json={
                "model": "mistralai/mistral-7b-instruct",  # You can change model here
                "messages": st.session_state.chat_history
            }
        )

        if response.status_code == 200:
            reply = response.json()["choices"][0]["message"]["content"]
            st.session_state.chat_history.append({"role": "assistant", "content": reply})
        else:
            st.error(f"Error: {response.status_code} - {response.text}")

    except Exception as e:
        st.error(f"❌ API call failed: {e}")


# Display chat history
for msg in st.session_state.chat_history[1:]:
    speaker = "You" if msg["role"] == "user" else "Bot"
    st.write(f"**{speaker}:** {msg['content']}")

# Add a button to clear chat history
if st.button("Clear Chat History"):
    st.session_state.chat_history = [{"role": "system", "content": "You are a helpful assistant."}]
    st.rerun()
  # Rerun the app to refresh the state