import streamlit as st
import read_person_data
import ekgdata
import matplotlib.pyplot as plt
import json

#%% Zu Beginn

# Lade alle Personen

person_names = read_person_data.get_person_list(read_person_data.load_person_data())

# Anlegen diverser Session States
## Gewählte Versuchsperson
if 'aktuelle_versuchsperson' not in st.session_state:
    st.session_state.aktuelle_versuchsperson = 'None'

## Anlegen des Session State. Bild, wenn es kein Bild gibt
if 'picture_path' not in st.session_state:
    st.session_state.picture_path = '../data/pictures/none.jpg'

#------------------------------------------------
## TODO: Session State für Pfad zu EKG Daten 
if 'ekg_data_path' not in st.session_state:
    st.session_state.ekg_data_path = '../data/ekg_data/01_Ruhe.txt'




#%% Design des Dashboards

# Schreibe die Überschrift
st.write("# EKG APP")
st.write("## Versuchsperson auswählen")

# Auswahlbox, wenn Personen anzulegen sind
st.session_state.aktuelle_versuchsperson = st.selectbox(
    'Versuchsperson',
    options = person_names, key="sbVersuchsperson")

# Name der Versuchsperson
st.write("Der Name ist: ", st.session_state.aktuelle_versuchsperson) 
# Pfad
st.write("Bildpfad: ", st.session_state.picture_path)
st.write("Pfad zu den EKG-Daten: ", st.session_state.ekg_data_path)

#-------------
if st.session_state.aktuelle_versuchsperson in person_names:
    st.session_state.picture_path = read_person_data.find_person_data_by_name(st.session_state.aktuelle_versuchsperson)["picture_path"]



# TODO: Weitere Daten wie Geburtsdatum etc. schön anzeigen

# Nachdem eine Versuchsperson ausgewählt wurde, die auch in der Datenbank ist
# Finde den Pfad zur Bilddatei
if st.session_state.aktuelle_versuchsperson in person_names:
    st.session_state.picture_path = read_person_data.find_person_data_by_name(st.session_state.aktuelle_versuchsperson)["picture_path"]
    # st.write("Der Pfad ist: ", st.session_state.picture_path) 


# Finde den Pfad zur Bilddatei und andere Daten
if st.session_state.aktuelle_versuchsperson in person_names:
    person_data = read_person_data.find_person_data_by_name(st.session_state.aktuelle_versuchsperson)
    st.session_state.picture_path = person_data["picture_path"]
    st.session_state.birth_date = person_data.get("date_of_birth", "Unbekannt")
    st.session_state.firstname = person_data.get("firstname", "Unbekannt")
    st.session_state.lastname = person_data.get("lastname", "Unbekannt")

    # Weitere Daten anzeigen
    st.write("### Weitere Informationen")
    st.write("**Vorname:**", st.session_state.firstname)
    st.write("**Nachname:**", st.session_state.lastname)
    #st.write("**Alter:**", person_data["age"])
    st.write("**Geburtsdatum:**", st.session_state.birth_date)
    st.write("**ID:**", person_data["id"])
    #st.write("**Maximale Herzfrequenz:**", person_data["max_hr"])
    #st.write("**Durchnittliche Herzfrequenz:**", person_data["average_hr"])
    #st.write("**Bildpfad:**", st.session_state.picture_path)





#%% Bild anzeigen

from PIL import Image
image = Image.open(st.session_state.picture_path)
st.image(image, caption=st.session_state.aktuelle_versuchsperson)

#% Öffne EKG-Daten
# TODO: Für eine Person gibt es ggf. mehrere EKG-Daten. Diese müssen über den Pfad ausgewählt werden können
# Vergleiche Bild und Person

#current_egk_data = ekgdata.EKGdata(r"data\ekg_data\01_Ruhe.txt")
current_egk_data = ekgdata.EKGdata(st.session_state.ekg_data_path)











#%% EKG-Daten als Matplotlib Plot anzeigen
# Nachdem die EKG, Daten geladen wurden
# Erstelle den Plot als Attribut des Objektes
current_egk_data.plot_time_series()
# Zeige den Plot an
st.pyplot(fig=current_egk_data.fig)


# %% Herzrate bestimmen
# Schätze die Herzrate 
current_egk_data.estimate_hr()
# Zeige die Herzrate an
st.write("Herzrate ist: ", int(current_egk_data.heat_rate)) 
