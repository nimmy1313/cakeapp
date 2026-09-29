import streamlit as st
from menu_loader import load_menu
from llm_utils import send_message_to_llm,start_session

CAKE_MENU=load_menu()
print(repr(CAKE_MENU))
st.title("🍰Home Bakery AI Assistant🍰")
st.markdown("Serving Dubai and Sharjah|Homemade Cakes|Payment on Delivery")
if "messages" not in st.session_state:
    start_session()
    welcome_message=(
        "Hi there!Welcome to Nims World Cakes\n\n"
        "Here is our Menu:\n\n"
        +CAKE_MENU
        +"\n Would you like to place an order?"
    )
    st.session_state.messages=[
        {
            "role":"Assistant",
            "context":welcome_message
        }
    ]
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["context"])
user_input=st.chat_input("Enter your message...")

if user_input:
    with st.chat_message("user"):
        st.markdown(user_input)
    st.session_state.messages.append(
        {
            "role":"user",
            "context":user_input
        }
    )
    llm_response=send_message_to_llm(user_input)
    with st.chat_message("assistant"):
        st.markdown(llm_response)
    st.session_state.messages.append(
        {
            "role":"assistant",
            "context":llm_response
        }
    )

