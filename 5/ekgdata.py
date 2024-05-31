import json
import pandas as pd
from person import Person
import plotly.express as px
import numpy as np   

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
        self.peaks_ekg = []

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
    

    @staticmethod   
    
    def find_peaks(series, threshold, respacing_factor=5):

        # Respace the series
        series = series.iloc[::respacing_factor]
    
        # Filter the series
        series = series[series>threshold]

        peaks = []
        last = 0
        current = 0
        next = 0

        for index, row in series.items():
            last = current
            current = next
            next = row

            if last < current and current > next and current > threshold:
                peaks.append(index-respacing_factor)

        
        return peaks
        
    def peaks_as_attribute(self, peaks):
        self.peaks_ekg = peaks
        return self.peaks_ekg
    

    def estimate_hr(self, peaks, sampling_rate):
        # Calculate time differences between peaks
        time_difference = [(peaks[i] - peaks[i-1]) / sampling_rate for i in range(1, len(peaks))]

        # Calculate average time difference
        avg_time_difference = sum(time_difference) / len(time_difference)

        # Calculate heart rate (beats per minute)
        heart_rate = 60 / avg_time_difference

        return heart_rate
    
    def plot_time_series(self, peaks):
        df.loc[:, "is_peak"] = False
        df.loc[peaks, "is_peak"] = True
        fig = px.scatter(df.iloc[0:5000], x='Time in ms', y='EKG in mV', color='is_peak') 
        return fig 

        

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
    #------------------------------------------------------------
    df = pd.read_csv(r'data/ekg_data/01_Ruhe.txt', sep='\t', header=None, names=['EKG in mV','Time in ms',])
    peaks = EKGdata.find_peaks(df["EKG in mV"].copy(), 340, 5)
    #print(peaks)
    # peaks als Attribut der Klasse EKGdata hinzufügen
    ekg.peaks_as_attribute(peaks)
    print(ekg.peaks_ekg)
    #------------------------------------------------------------
    heart_rate = ekg.estimate_hr(peaks, 1000)
    print("Heart Rate: ", heart_rate)
    #------------------------------------------------------------
    fig = ekg.plot_time_series(peaks)
    fig.show() 



    

    
    


# %%
