import streamlit as st

if "loggedIn" not in st.session_state:
    st.session_state["loggedIn"] = False


def calorietracker():
    if "foods" not in st.session_state:
        st.session_state["foods"] = []
    if "total_calories" not in st.session_state:
        st.session_state["total_calories"] = 0

    food = st.text_input("Nahrungsmittel")
    calories = st.number_input("Kalorien", min_value=0)
    if st.button("Hinzufügen"):
        st.session_state["foods"].append({"food": food, "calories": calories})
        st.session_state["total_calories"] += calories

    st.write("Gesamtkalorien:", st.session_state["total_calories"])
    st.write("Nahrungsmittel:")
    for item in st.session_state["foods"]:
        st.write(f"{item['food']}: {item['calories']} Kalorien")
    
    

st.title("Kalorientracker")

if st.session_state["loggedIn"]:
    calorietracker() 
else:
    st.markdown("Logge dich ein, um den Kalorienrtracker zu nutzen.")