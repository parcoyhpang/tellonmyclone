import streamlit as st
import random
import database as db
st.set_page_config(page_title="TestProj", page_icon=":lemon:", layout="centered")
st.title("Yes, it's a cheap knockoff of Tellonym.")
st.info('Wanted to challenge myself to code and deploy this in under an hour.', icon="ℹ️")
st.markdown("")
input_text = st.text_area("So... talk to me:", height=100, max_chars=250, key=None)
submitted = st.button("Submit")
note = """
1.  This is a demo app, so don't expect it to be secure.
2.  It's **truly anonymous** because I didnt bother to code any spying thingys.
3.  Entirely coded in Python, so *kinda* cool.
4.  Try not to pan test it, I'm not paying for the server.
5.  I do have a filter but still please don't spam me.
"""
st.markdown(note)
st.info("Repo for this project available on [GitHub]().")
st.markdown("[Parco YH Pang](https://parcopang.com) © 2022. ")

if submitted:
    if input_text == "":
        st.error("Nice try, it's empty.")
    else:
        with st.spinner("Posting..."):
            mid = ''.join([str(random.randint(0, 999)).zfill(3) for _ in range(2)])
            db.insert(input_text, mid)
        st.success("Message sent!")
hide_streamlit_style = """<style>footer {visibility: hidden;} #MainMenu {visibility: hidden}</style>"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)