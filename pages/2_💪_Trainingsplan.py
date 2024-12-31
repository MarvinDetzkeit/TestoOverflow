import streamlit as st
import json
import os

#Variable declarations

if "loggedIn" not in st.session_state:
    st.session_state["loggedIn"] = False

if "modeT" not in st.session_state:
    st.session_state["modeT"] = 0

if "workoutPlan" not in st.session_state and st.session_state["loggedIn"]:
    if os.path.exists("JSONs/Trainingsplan_" + st.session_state["user"] + ".json"):
        with open("JSONs/Trainingsplan_" + st.session_state["user"] + ".json", "r") as plan:
            st.session_state["workoutPlan"] = json.load(plan)
    else:
        st.session_state["workoutPlan"] = {}

# Procedures

def switchMode(m):
    st.session_state["modeT"] = m
    st.rerun()

# mode 0

def emptyPlan():
    if len(st.session_state["workoutPlan"]) > 0:
        switchMode(2)
    else:
        st.markdown("Erstelle einen Trainingsplan!")
        if st.button("Erstellen"):
            switchMode(1)

# mode 1
def createWorkoutPlan():
    showWorkoutPlan()
    name = st.text_input("Name der Übung", "")
    sets = st.slider("Anzahl der Sätze", 1, 10)
    if st.button("Hinzufügen") and name and (name not in st.session_state["workoutPlan"]):
        st.session_state["workoutPlan"][name] = sets
        st.rerun()
    st.divider()
    if st.button("Speichern"):
        if len(st.session_state["workoutPlan"]) > 0:
            with open("JSONs/Trainingsplan_" + st.session_state["user"] + ".json", "w") as jsonfile:
                json.dump(st.session_state["workoutPlan"], jsonfile, indent=4)
            switchMode(2)
        else:
            st.error("Füge mindestens eine Übung zum Plan hinzu")

# mode 2
def workoutExists():
    showWorkoutPlan()
    st.divider()
    st.markdown("Übungen hinzufügen")
    if st.button("Hinzufügen"):
        switchMode(1)
    st.divider()
    st.markdown("Plan löschen und neu erstellen")
    if st.button("Löschen"):
        st.session_state["workoutPlan"] = {}
        with open("JSONs/Trainingsplan_" + st.session_state["user"] + ".json", "w") as jsonfile:
            json.dump(st.session_state["workoutPlan"], jsonfile, indent=4)
        switchMode(1)

def showWorkoutPlan():
    if len(st.session_state["workoutPlan"]) < 1:
        return
    tabelle = "| Übung | Sätze |\n"
    tabelle += "|-----------|------|\n"
    for key, value in st.session_state["workoutPlan"].items():
        tabelle += f"| {key} | {value} |\n"
    st.markdown(tabelle)
    

    

st.title("Trainingsplan")

if not st.session_state["loggedIn"]:
    st.markdown("Logge dich ein, um den Trainingsplan zu nutzen.")
elif st.session_state["modeT"] == 0:
    emptyPlan()
elif st.session_state["modeT"] == 1:
    createWorkoutPlan()
elif st.session_state["modeT"] == 2:
    workoutExists()