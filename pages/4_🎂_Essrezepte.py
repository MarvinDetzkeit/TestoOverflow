import streamlit as st

# Variable declarations
st.title("Essrezepte")



if "loggedIn" not in st.session_state:
    st.session_state["loggedIn"] = False

if st.session_state["loggedIn"]:
    st.write("Trainiere dich 3 mal, um ein neues Rezept freizuschalten")

# Übungen sind zu Beginn noch nicht abgeschlossen
if "excercises_completed" not in st.session_state:
    st.session_state["excercises_completed"] = 0

# Rezepte sind noch nicht freigeschaltet
if "recipes_unlocked" not in st.session_state:
    st.session_state["recipes_unlocked"] = False

# Funktion um Übungspunkte zu erhöhen
def complete_exercise():
    st.session_state["excercises_completed"] += 1




# UI Interface
st.title("Übungen und Belohnungen")

# Zeige die Anzahl der Übungen an
st.write(f"Du hast bisher {st.session_state['excercises_completed']} Übungen abgeschlossen.")


# Funktion um Rezepte freizuschalten
def unlock_yummies():
 completed=st.session_state["excercises_completed"]
 unlocked_recipes= completed // 3
 st.session_state["recipes_unlocked"]=unlocked_recipes

 if unlocked_recipes > 0 and completed % 3 == 1 :

  st.write("Herzlichen Glückwunsch! Du hast aufgrund deiner starken Bemühungen folgendes Rezept verdient 🎉✨")


recipes=["Rezept 1: Gesunde Avocado-Bowl---> Zutaten: 1 reife Avocado, 1 kleine Tomate, 1/4 Gurke, 1 Esslöffel Olivenöl, Saft von 1/2 Zitrone, Salz und Pfeffer nach Geschmack, 1 Teelöffel Sesam (optional) ---👨‍🍳Zubereitung: Die Avocado schälen und in kleine Stücke schneiden. Tomate und Gurke ebenfalls klein schneiden. Alles in einer Schüssel anrichten und mit Olivenöl und Zitronensaft beträufeln. Mit Salz und Pfeffer abschmecken und nach Wunsch mit Sesam bestreuen.  ", "Rezept 2: Falafel mit Hummus" " Zutaten für Falafel: 1 Dose Kichererbsen (oder 200g gekochte Kichererbsen), 1 kleine Zwiebel, 2 Knoblauchzehen, 1/2 Teelöffel Kreuzkümmel, 1/2 Teelöffel Paprikapulver, Salz und Pfeffer, 1/4 Tasse frische Petersilie,2 Esslöffel Mehl Öl zum Frittieren , Zutaten für Hummus: 1 Dose Kichererbsen, 2 Esslöffel, Tahini, 2 Esslöffel Zitronensaft, 1 Knoblauchzehe, 2 Esslöffel, Olivenöl, Salz und Pfeffer nach Geschmack , ---👨‍🍳Zubereitung: Alle Zutaten für die Falafel in einer Küchenmaschine pürieren, bis eine formbare Masse entsteht. Kleine Bällchen formen und in heißem Öl frittieren, bis sie goldbraun sind. Für den Hummus alle Zutaten in einer Küchenmaschine pürieren, bis eine glatte Creme entsteht. Falafel mit Hummus servieren.", "Rezept 3: Quinoa-Salat mit geröstetem Gemüse: Zutaten: 1 Tasse Quinoa 1 Zucchini 1 Paprika 1 kleine Aubergine 1/2 rote Zwiebel Olivenöl Salz, Pfeffer und Kräuter nach Geschmack 1 Handvoll frische Petersilie 1 Esslöffel Balsamico-Essig, ---👨‍🍳Zubereitung: Quinoa nach Packungsanweisung kochen. Zucchini, Paprika, Aubergine und Zwiebel in Würfel schneiden und mit Olivenöl, Salz und Pfeffer vermengen. Gemüse auf einem Backblech verteilen und bei 200°C im Ofen für 20 Minuten rösten. Quinoa mit dem gerösteten Gemüse und frischer Petersilie vermengen. Mit Balsamico-Essig beträufeln und servieren.", "Rezept 4: Thunfisch Salat: Zutaten: 1 Dose Thunfisch in Wasser (abgetropft) 1/2 rote Zwiebel 1 kleine Gurke 1 Handvoll Cherry-Tomaten 1 Esslöffel Olivenöl 1 Teelöffel Senf Saft von 1/2 Zitrone Salz und Pfeffer nach Geschmack 1 Handvoll frische Petersilie, ---👨‍🍳Zubereitung: Thunfisch abtropfen lassen und in eine Schüssel geben. Zwiebel und Gurke klein schneiden, Tomaten halbieren. Alles in die Schüssel geben und mit Olivenöl, Senf, Zitronensaft, Salz und Pfeffer vermengen. Mit frischer Petersilie garnieren und servieren."]


#zeige nur die unlocked rezepte

for i in range(st.session_state["recipes_unlocked"]):
    st.write(recipes[i])

# Button um Übung abzuschließen
if st.button("Übung abschließen"):
    complete_exercise()
    unlock_yummies()

