import pandas as pd
import numpy as np
import plotly.express as px


# Read Activity Data
def read_activity_csv():
    path = "data/activities/activity.csv"
    df = pd.read_csv(path)
    return df

def find_best_effort(df, t_intervall, fs): # fs = Anzahl der Werte pro Sekunde | t_intervall = Zeitintervall in Sekunden
    #todo find best effort
    # find the interval with the highest mean power
    # t_intervall: length of the interval in seconds
    # fs: sampling frequency of the data
    N = len(df)
    window_size = int(t_intervall*fs)
    rolling_power = df["PowerOriginal"].rolling(window = window_size).mean()

    best_power = rolling_power.max()

    return best_power




def create_power_curve(df, intervall_list, fs):
    intervalls_max_power = []
    for intervall in intervall_list:
        #find_best_effort(df, intervall, fs)
        intervalls_max_power.append(find_best_effort(df, intervall, fs))

    max_power_df = pd.DataFrame(
    {'TimeIntervall': intervall_list, 
     'MaxPower': intervalls_max_power
     })
           
    return max_power_df
    




'''
    best_effort = 0
    best_effort_power = 0
    for i in range(0, N-n):
        p_mean = df["PowerOriginal"][i:i+n].mean()
        if p_mean > best_effort_power:
            best_effort_power = p_mean
            best_effort = i
    return best_effort 
'''





# main
if __name__ == "__main__":
    df = read_activity_csv()
    best_power = find_best_effort(df, 30, 1)
    print(best_power)
    df["BestPower"] = best_power
    #print(df.head())
#------------------------------------------------------------
    intervall_list = [1, 30, 60, 120, 300, 600, 1200, 1800] # Zeitintervalle in Sekunden 1s - 30min
    fs = 1 # Anzahl der Werte pro Sekunde
    print(create_power_curve(df, intervall_list, fs))
