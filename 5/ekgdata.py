import json
import pandas as pd
from person import Person
import plotly.express as px
from scipy.signal import find_peaks   
import matplotlib.pyplot as plt

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
        self.peaks = self.find_peaks()
        #self.estimate_HR = self.estimate_hr()
        self.estimated_hr = self.estimate_hr()
        self.fig = self.plot_time_series()

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
                if str(ekg_test["id"]) == such_id:
                    return ekg_test
        return {}
    


    def find_peaks(self):
        # Find peaks in the EKG data
        peaks  = find_peaks(self.df['EKG in mV'], height=330, distance=200, prominence=60)
        return peaks
    

    '''def estimate_hr(self, peaks, sampling_rate):
        # Calculate time differences between peaks
        time_difference = [(peaks[i] - peaks[i-1]) / sampling_rate for i in range(1, len(peaks))]
        # Calculate average time difference
        avg_time_difference = sum(time_difference) / len(time_difference)
        # Calculate heart rate (beats per minute)
        heart_rate = 60 / avg_time_difference

        return heart_rate'''
    
    #tobi
    
    def estimate_hr(self):
        self.estimated_hr_list = []
        peaks_times = self.df['Time in ms'][self.peaks]
        for i in range(1, len(peaks_times)):
            difference = (peaks_times.iloc[i] - peaks_times.iloc[i-1])/500*60
            self.estimated_hr_list.append(difference)
        self.estimated_hr = sum(self.estimated_hr_list)/len(self.estimated_hr_list)
        return self.estimated_hr
    
    '''def plot_time_series(self, peaks):
        df.loc[:, "is_peak"] = False
        df.loc[peaks, "is_peak"] = True
        fig = px.scatter(df.iloc[0:5000], x='Time in ms', y='EKG in mV', color='is_peak') 
        return fig 
    '''

    def plot_time_series(self):
        fig, ax = plt.subplots()
        ax.set_xlabel('Time in ms')
        ax.set_ylabel('EKG in mV')
        ax.set_title('EKG Time Series with Peaks')
        ax.plot(self.df['Time in ms'], self.df['EKG in mV'])
        ax.scatter(self.df['Time in ms'][self.peaks], self.df['EKG in mV'][self.peaks], color='red')
        return fig
'''
        plt.figure(figsize=(12, 6))
        plt.plot(self.df['Time in ms'], self.df['EKG in mV'], color='blue')
        plt.scatter(self.df['Time in ms'][self.peaks], self.df['EKG in mV'][self.peaks], color='red', marker='x')
        plt.xlabel('Time in ms')
        plt.ylabel('EKG in mV')
        plt.title('EKG Time Series with Peaks')
        plt.show()'''
        
      

        

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
    peaks, _ = find_peaks(df['EKG in mV'], height=0)
    
    
    #------------------------------------------------------------
    heart_rate = ekg.estimate_hr(peaks, 1000)
    print("Heart Rate: ", heart_rate)
    #------------------------------------------------------------
    fig = ekg.plot_time_series(peaks)
    fig.show() 
    #------------------------------------------------------------


    

    
    


# %%
