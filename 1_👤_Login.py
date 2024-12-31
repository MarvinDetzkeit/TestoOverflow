import streamlit as st
import json

#Variable declarations

if "loggedIn" not in st.session_state:
    st.session_state["loggedIn"] = False

if "userList" not in st.session_state:
    with open("JSONs/userList.json", "r") as u:
        st.session_state["userList"] = json.load(u)

# Procededures

def loginScreen():
    username = st.text_input("Nutzername")
    if username:
        st.session_state["username"] = username
        if username == st.session_state["userList"]["user0"]:
            st.session_state["loggedIn"] = True
            st.session_state["user"] = "user0"
            st.rerun()
        elif username == st.session_state["userList"]["user1"]:
            st.session_state["loggedIn"] = True
            st.session_state["user"] = "user1"
            st.rerun()
        else:
            st.error("Ungültiger Nutzername")


    

st.title("Login")

if st.session_state["loggedIn"]:
    st.markdown("Herzlich Willkommen " + st.session_state["username"])
else:
    loginScreen()