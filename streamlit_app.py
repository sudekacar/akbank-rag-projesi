import streamlit as st
from rag_backend import answer

st.set_page_config(page_title="Akbank Finans Asistanı", page_icon="💬")
st.title("Akbank Finans Asistanı (Gemini + RAG)")

if "history" not in st.session_state: st.session_state.history = []
for role, msg in st.session_state.history:
    with st.chat_message(role): st.markdown(msg)

prompt = st.chat_input("Sorunu yaz…")
if prompt:
    st.session_state.history.append(("user", prompt))
    with st.chat_message("assistant"):
        with st.spinner("Gemini düşünüyor…"):
            reply = answer(prompt)
            st.markdown(reply)
            st.session_state.history.append(("assistant", reply))
