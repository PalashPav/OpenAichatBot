# import streamlit as st
# import openai

# # Set up the Streamlit app
# st.title("Jarvis")

# # Connect to OpenAI API
# openai.api_key = st.secrets["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"]

# # Initialize chat history
# chat_history = []

# # Create a text input for the user's message
# user_input = st.text_input("Type your message here:")

# # Create a button to submit the message
# submit_button = st.button("Send")

# if submit_button:
#     # Add the user's message to the chat history
#     chat_history.append(("User", user_input))
    
#     # Generate a response from the OpenAI API using the chat.completions.create method
#     response = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo-0125",
#         response_format={"type": "json_object"},
#         messages=[
#             {"role": "system", "content": "You are a helpful assistant designed to output JSON."},
#             *[{"role": role, "content": content} for role, content in chat_history]
#         ]
#     )
    
#     # Add the bot's response to the chat history
#     chat_history.append(("Bot", response['choices'][0]['message']['content']))
    
#     # Clear the text input
#     st.text_input("Type your message here:", value="", key="user_input")

# # Display the chat history
# for sender, message in chat_history:
#     st.write(f"{sender}: {message}")

import streamlit as st
from openai import OpenAI

# Initialize the OpenAI client with your API key
client = OpenAI(api_key="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")

def generate_response(prompt):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
            {"role": "user", "content": prompt},
        ]
    )
    # Correctly access the 'content' attribute of the message
    return completion.choices[0].message.content

st.title("Chatbot")
user_input = st.text_input("Type your message here:")
if st.button("Send"):
    response = generate_response(user_input)
    st.write(f"Bot: {response}")