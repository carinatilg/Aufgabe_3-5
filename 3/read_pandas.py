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
    df["zone1"] = df["HeartRate"] > zone_1_min and df["HeartRate"] < zone_1_max

    return df

#def compute_time_zones(df):
    #compute the time in zone 1 etc.

    return[t_1, t_2, ...]

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


#%% Test

#df = read_my_csv()
#fig = make_plot(df)

#fig.show()
