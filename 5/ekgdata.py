import json
import pandas as pd
from person import Person

# %% Objekt-Welt

# Klasse EKG-Data für Peakfinder, die uns ermöglicht peaks zu finden

class EKGdata:

## Konstruktor der Klasse soll die Daten einlesen

    def __init__(self, ekg_dict):
        pass
        self.id = ekg_dict["id"]
        self.date = ekg_dict["date"]
        self.data = ekg_dict["result_link"]
        self.df = pd.read_csv(self.data, sep='\t', header=None, names=['EKG in mV','Time in ms',])

# %% Test
    @staticmethod
    def load_by_id(such_id):
    # für alle ekg test über alle personen
    # for pereon in prsons
    #for ekgtest in test    def load_by_id(such_id):

        person_data = Person.load_person_data()

        if such_id == "None":
            return {}
        
        for eintrag in person_data:
            for ekg_test in eintrag["ekg_tests"]:
                if (ekg_test["id"] == such_id):
                    return ekg_test
        return {}
       

        
        

if __name__ == "__main__":
    print("This is a module with some functions to read the EKG data")
    file = open("data/person_db.json")
    person_data = json.load(file)
    ekg_dict = person_data[0]["ekg_tests"][0]
    print(ekg_dict)
    ekg = EKGdata(ekg_dict)
    print(ekg.df.head())
    #------------------------------------------------------------
    ekg_data = EKGdata.load_by_id(1)
    print("Eintrag von gewählter ID EKG:", ekg_data) #id


# %%
