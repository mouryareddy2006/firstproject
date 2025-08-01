import streamlit as st
st.title("Mourya's file")
st.header("welcome")
st.write("python programme")

name=st.text_input("enter your name:")
if name:
   st.success(f"hello,{name}! how are you?,My name is Mourya how can i help you. Im currently pursuing my B.Tech and Im from Hyderabad,I have a strong interest in coding and Im always eager to learn new things in the world of technology. Thats one of the reasons Im here — Im looking forward to getting some coding tasks and challenges to improve my skill Im excited to connect with people who share similar interests and grow together")




number=st.slider("pick your age",0,100)
st.write(f"your age is {number}")

rat=st.text_input("enter your email:")
if rat:
   st.success(f"we have sent verification code to your email ,{rat}")


