import streamlit as st
num = st.slider("choose ur number",1,100)
st.write('square of ', num, 'is', num ** 2)