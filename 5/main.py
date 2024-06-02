import streamlit as st
import read_person_data
import ekgdata
import matplotlib.pyplot as plt
import json
import person

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
#st.write("Bildpfad: ", st.session_state.picture_path)
#st.write("Pfad zu den EKG-Daten: ", st.session_state.ekg_data_path)

#-------------
if st.session_state.aktuelle_versuchsperson in person_names:
    st.session_state.picture_path = read_person_data.find_person_data_by_name(st.session_state.aktuelle_versuchsperson)["picture_path"]



# TODO: Weitere Daten wie Geburtsdatum etc. schön anzeigen

# Nachdem eine Versuchsperson ausgewählt wurde, die auch in der Datenbank ist
# Finde den Pfad zur Bilddatei
if st.session_state.aktuelle_versuchsperson in person_names:
    st.session_state.picture_path = read_person_data.find_person_data_by_name(
        st.session_state.aktuelle_versuchsperson)["picture_path"]
    
    # Lade die Daten der Versuchsperson
    anwender = person.Person.load_person_data()
    for person_data in anwender:
        if person_data["lastname"] + ", " + person_data["firstname"] == st.session_state.aktuelle_versuchsperson:
            current_person = person.Person(person_data)
            break

    # Speichere die Daten in Session States
    st.header("Personendaten:")
    st.write("ID: ", current_person.id)
    st.write("Vorname: ", current_person.firstname)
    st.write("Nachname: ", current_person.lastname)
    st.write("Geburtsdatum: ", current_person.date_of_birth)
    st.write("Alter: ", current_person.age)
    st.write("Maximale Herzfrequenz: ", current_person.max_heart_rate)
    st.write("EKG-Daten: ", current_person.ecg_data)


#%% Bild anzeigen

from PIL import Image
image = Image.open(st.session_state.picture_path)
st.image(image, caption=st.session_state.aktuelle_versuchsperson)

#% Öffne EKG-Daten
# TODO: Für eine Person gibt es ggf. mehrere EKG-Daten. Diese müssen über den Pfad ausgewählt werden können
# Vergleiche Bild und Person


# Öffne EKG-Daten
if 'current_person' in locals():
    if len(current_person.ecg_data) > 1:
        option = st.selectbox("EKG auswählen: ", options= [1, 2], key="sbEKG")
        current_ekg = ekgdata.EKGdata(current_person.ecg_data[option-1])

    else:
        current_ekg = current_ekg = ekgdata.EKGdata(current_person.ecg_data[0])
    st.write("Geschätzte Herzfrequenz: ", int(current_ekg.estimated_hr))

    # EKG-Daten anzeigen
    #st.plotly_chart(current_ekg.fig)
    st.pyplot(current_ekg.fig)
else:
    st.write("Bitte wählen Sie eine Versuchsperson aus.")






current_ekg_data = ekgdata.EKGdata(current_person.ecg_data)




#%% EKG-Daten als Matplotlib Plot anzeigen
# Nachdem die EKG, Daten geladen wurden
# Erstelle den Plot als Attribut des Objektes
current_ekg_data.plot_time_series()

# Zeige den Plot an
st.pyplot(fig=current_ekg_data.fig)


# %% Herzrate bestimmen
# Schätze die Herzrate 
current_ekg_data.estimate_hr()
# Zeige die Herzrate an
st.write("Herzrate ist: ", int(current_ekg_data.heart_rate)) 
