import streamlit as st

st.title("CPIMS Chatbot")

user_input = st.text_input("You:", "")
bot_response = st.empty()

if st.button("Send"):
    bot_response.text("Bot: Hi there!")
import rasa
from rasa.core.agent import Agent

model_path = "path/to/your/model"
agent = Agent.load(model_path)

def generate_response(user_input):
    response = agent.handle_text(user_input)
    return response[0]["text"]

user_input = st.text_input("You:", "")
bot_response = st.empty()

if st.button("Send"):
   bot_response.text("Bot: " + generate_response(user_input))

   

