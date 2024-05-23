# %%

# Paket für Bearbeitung von Tabellen
import pandas as pd
import numpy as np

# Paket
## zuvor !pip install plotly
## ggf. auch !pip install nbformat
import plotly.express as px


def read_my_csv():
    # Einlesen eines Dataframes
    ## "\t" steht für das Trennzeichen in der txt-Datei (Tabulator anstelle von Beistrich)
    ## header = None: es gibt keine Überschriften in der txt-Datei
    df = pd.read_csv("data/ekg_data/01_Ruhe.txt", sep="\t", header=None)

    # Setzt die Columnnames im Dataframe
    df.columns = ["Messwerte in mV","Zeit in ms"]
    
    # Gibt den geladen Dataframe zurück
    return df

# Read Activity Data
def read_activity_csv():
    path = "data/activities/activity.csv"
    df = pd.read_csv(path)

    N=len(df)
    df['time'] = np.array(range(N))
    print(df["time"])


    return df

# 
def compute_power_statistics(df):
    #todo compute mean and max
    p_mean = df["PowerOriginal"].mean()
    p_max = df["PowerOriginal"].max()
    return p_mean, p_max

def plot_pow_HR(df):
    #todo make plot
    fig = px.line(df, x="time", y=['PowerOriginal', 'HeartRate'])
    
    return fig

def compute_HR_max(df):
    HR_max = df["HeartRate"].max() 
    return HR_max

def add_HR_zones(df, HR_max):
    #todo commpute zone boundaries
    zone_1_min = HR_max * 0.5 # 50%
    zone_1_max = HR_max * 0.6 # 60%
    zone_2_max = HR_max * 0.7 # 70%
    zone_3_max = HR_max * 0.8 # 80%
    zone_4_max = HR_max * 0.9 # 90%
    zone_5_max = HR_max # 100%

    #todo add columns to df
    zone1_condition = (df["HeartRate"] > zone_1_min) & (df["HeartRate"] < zone_1_max)
    zone2_condition = (df["HeartRate"] > zone_1_max) & (df["HeartRate"] < zone_2_max)
    zone3_condition = (df["HeartRate"] > zone_2_max) & (df["HeartRate"] < zone_3_max)
    zone4_condition = (df["HeartRate"] > zone_3_max) & (df["HeartRate"] < zone_4_max)
    zone5_condition = (df["HeartRate"] > zone_4_max) & (df["HeartRate"] < zone_5_max)

    df["zone1"] = np.where(zone1_condition, 1, 0)
    df["zone2"] = np.where(zone2_condition, 1, 0) 
    df["zone3"] = np.where(zone3_condition, 1, 0)
    df["zone4"] = np.where(zone4_condition, 1, 0)
    df["zone5"] = np.where(zone5_condition, 1, 0)

    return df

def compute_time_zones(df):
    #compute the time in zone 1 etc.

    t_1 = sum(df["zone1"]) # time in zone 1
    t_2 = sum(df["zone2"]) # time in zone 2
    t_3 = sum(df["zone3"]) # time in zone 3
    t_4 = sum(df["zone4"]) # time in zone 4
    t_5 = sum(df["zone5"]) # time in zone 5
    

    return[t_1, t_2, t_3, t_4, t_5]

#def compute_power_in_zone(df):
    # todo compute power per zone

    retrun[p_1, p_2,...]




# %%
def make_plot(df):

    # Erstellte einen Line Plot, der ersten 2000 Werte mit der Zeit aus der x-Achse
    fig = px.line(df.head(2000), x= "Zeit in ms", y="Messwerte in mV")
    return fig

if __name__ == "__main__":
    df = read_activity_csv()
    #------------------------------------------------
    p_mean, p_max = compute_power_statistics(df)
    print('p_mean:',p_mean)
    print('p_max:',p_max)
    #------------------------------------------------
    fig = plot_pow_HR(df)
    fig.show()
    #------------------------------------------------
    HR_max = compute_HR_max(df)
    #------------------------------------------------
    add_HR_zones(df, 220)
    t_1, t_2, t_3, t_4, t_5 = compute_time_zones(df)
    print(t_1, t_2, t_3, t_4, t_5)

#%% Test

#df = read_my_csv()
#fig = make_plot(df)

#fig.show()
