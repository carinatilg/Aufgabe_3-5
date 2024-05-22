# %%

# Paket für Bearbeitung von Tabellen
import pandas as pd

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

def read_activity_csv():
    path = "data/activities/activity.csv"
    df = pd.read_csv(path)
    return df

def compute_power_statistics(df):
    #todo compute mean and max

    return p_mean, p_max

def plot_pow_HR(df):
    #todo make plot

    return fig 

def add_HR_zones(df, ...):
    #todo cpmpute zone boundaries
    zone_1_min = ...
    zone_1_max = ...
    #todo add columns to df
    df["zone1"] = df["HeartRate"] > zone_1_min and df["HeartRate"] < zone_1_max

    return df

def compute_time_zones(df):
    #compute the time in zone 1 etc.

    return[t_1, t_2, ...]

def compute_power_in_zone(df):
    # todo compute power per zone

    retrun[p_1, p_2,...]




# %%
def make_plot(df):

    # Erstellte einen Line Plot, der ersten 2000 Werte mit der Zeit aus der x-Achse
    fig = px.line(df.head(2000), x= "Zeit in ms", y="Messwerte in mV")
    return fig

if __name__ == "__main__":
    df =read.activity.


#%% Test

#df = read_my_csv()
#fig = make_plot(df)

#fig.show()

# %%
