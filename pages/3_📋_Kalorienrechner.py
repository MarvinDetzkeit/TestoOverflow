import streamlit as st

#Variable declarations

if "loggedIn" not in st.session_state:
    st.session_state["loggedIn"] = False

# Procedures

def calorieCalculator():
    # get data
    sex = st.radio("Geschlecht", ("männlich", "weiblich"))
    age = st.slider("Alter", 10, 99)
    height = st.slider("Größe (cm)", 100, 250)
    weight = st.slider("Gewicht (kg)", 30, 300)
    activity = st.radio("Aktivitätslevel", ("Inaktiv",
                                            "Ein wenig Aktiv (1-3 mal pro Woche Sport)",
                                            "Aktiv (4-5 mal pro Woche Sport)",
                                            "Sehr Aktiv (6-7 mal pro Woche Sport)",
                                            "Extrem Aktiv (3-5 mal pro Woche Sport + Physischer Job)"))
    goal = st.radio("Trainingsziel", ("Cut", "Bulk", "Gewicht halten"))

    # calculate calories
    bmr = (10 * weight) + (6.25 * height) - (5 * age)
    if sex == "männlich":
        bmr += 5
    elif sex == "weiblich":
        bmr -= 161
    
    if activity == "Inaktiv":
        activityMultiplier = 1.2
    elif activity == "Ein wenig Aktiv (1-3 mal pro Woche Sport)":
        activityMultiplier = 1.375
    elif activity == "Aktiv (4-5 mal pro Woche Sport)":
        activityMultiplier = 1.55
    elif activity == "Sehr Aktiv (6-7 mal pro Woche Sport)":
        activityMultiplier = 1.725
    elif activity == "Extrem Aktiv (3-5 mal pro Woche Sport + Physischer Job":
        activityMultiplier = 1.9
    bmr *= activityMultiplier

    if goal == "Bulk":
        bmr *= 1.15
    elif goal == "Cut":
        bmr *= 0.85
    
    if st.button("Berechnen"):
        st.markdown("Ergebnis: " + str(int(bmr)) + " kcal")
    else:
        st.markdown("Ergebnis:")
    



st.title("Kalorienrechner")

if st.session_state["loggedIn"]:
    calorieCalculator()
else:
    st.markdown("Logge dich ein, um den Kalorienrechner zu nutzen.")