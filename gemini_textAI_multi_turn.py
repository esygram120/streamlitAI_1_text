# Reference : 
# Google Gemini API - https://ai.google.dev/tutorials/python_quickstart
# Google Gemini API (Multi-trun) message example
# messages = [
#     {'role':'user',
#      'parts': ["Briefly explain how a computer works to a young child."]},
#     {'role':'model', 'parts':[response.text]},
#     {'role':'user', 'parts':["Okay, how about a more detailed explanation to a high school student?"]}
# ]

# Streamlit + Google Gemini LLM

import streamlit as st
import google.generativeai as genai

with st.sidebar:
    "[홈으로 돌아가기](http://localhost:8080/)"
    gemini_api_key = st.text_input("Gemini API Key", key="chatbot_api_key", type="password")

st.title("🚀 텍스트 문답처리 서비스 💬")
st.caption("Streamlit + Google Gemini LLM 을 연동했습니다.")
st.caption("Multi-turn 기능 추가해서 가장 최근 것을 포함한 지난 기록을 모두 반영해 답변하는 서비스입니다.")
if "messages" not in st.session_state:
    st.session_state["messages"] = []

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["parts"][-1])

if prompt := st.chat_input():
    if not gemini_api_key:
        st.info("Google Gemini API 키를 입력하고 서비스를 이용해주세요.")
        st.stop()

    genai.configure(api_key=gemini_api_key)
    model = genai.GenerativeModel('gemini-pro')

    st.session_state.messages.append({"role": "user", "parts": [prompt]})
    st.chat_message("user").write(prompt)

    response = model.generate_content(st.session_state.messages)
    msg = response.text

    st.session_state.messages.append({"role": "model", "parts": [msg]})
    st.chat_message("model").write(msg)