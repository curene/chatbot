import streamlit as st
import random
import time

st.set_page_config(page_title="Ex-stream-ly Cool App")

st.title("Talk")

def get_reply(message):
    message = message.lower()

    if "안녕" in message or "hello" in message:
        return ("text", "안녕, 만나서 반가워.")
    elif "기분이 어때" in message:
        return ("text", get_random_mood())
    elif "cat" in message:
        img_url = get_cat_image_url()
        return ("image", img_url)
    elif "capital of afghanistan" in message:
        return ("text", "Kabul.")
    elif "capital of albania" in message:
        return ("text", "Tirana.")
    elif "capital of algeria" in message:
        return ("text", "Algiers.")
    elif "capital of andorra" in message:
        return ("text", "Andorra la Vella.")
    elif "capital of angola" in message:
        return ("text", "Luanda.")
    elif "capital of antigua & barbuda" in message:
        return ("text", "Saint John's.")
    elif "capital of argentina" in message:
        return ("text", "Buenos Aires.")
    elif "capital of armenia" in message:
        return ("text", "Yerevan.")
    elif "capital of australia" in message:
        return ("text", "Canberra.")
    elif "capital of austria" in message:
        return ("text", "Vienna.")
    elif "capital of azerbaijan" in message:
        return ("text", "Baku.")
    elif "capital of the bahamas" in message:
        return ("text", "Nassau.")
    elif "capital of bahrain" in message:
        return ("text", "manama.")
    elif "capital of bangladesh" in message:
        return ("text", "Dhaka.")
    elif "capital of barbados" in message:
        return ("text", "Bridgetown.")
    else:
        return ("text", "아직 무슨 말인지 모르겠어.")

def get_random_mood():
    mood = ["기분이 좋아.", "기분이 그저 그래.", "나쁘지 않아.", "행복해."]
    return random.choices(mood)[0]

def get_cat_image_url():
    return f"https://cataas.com/cat?time={time.time()}"

#user_input = st.text_input("message를 입력하세요")

if "chat_log" not in st.session_state:
    st.session_state.chat_log = []

# if st.button("SEND") and user_input:
#     # 사람 메시지 User message
#     st.session_state.chat_log.append(("You", user_input, "text"))
#     # 봇 메시지 Bot message
#     reply_type, bot_reply = get_reply(user_input)
#     st.session_state.chat_log.append(("Bot", bot_reply, reply_type))

# for role,msg,msg_type in st.session_state.chat_log:
#     if msg_type == "text":
#         st.write(f"**{role}:** {msg}")
#     elif msg_type == "image":
#         st.image(msg, width=300)

prompt = st.chat_input("메시지를 입력하세요")

if prompt:
    st.session_state.chat_log.append(("user", prompt, "text"))
    with st.chat_message("user"):
        st.write(prompt)
    
    reply_type, reply = get_reply(prompt)

    st.session_state.chat_log.append(("assistant", reply, reply_type))

    with st.chat_message("assistant"):
        if reply_type == "text":
            st.write(reply)
        else:
            st.image(reply, width=300)