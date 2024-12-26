import streamlit as st

st.header("Learning is FUN!!!!")

st.subheader("_Streamlit_ is :blue[cool] :sunglasses:")

code = '''def hello():
    print("Hello, Streamlit!")'''
st.code(code, language="python")