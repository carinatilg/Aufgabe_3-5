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


def make_plot_power_curve(max_power_df, intervall_list):
    
    #fig = px.line(max_power_df.head(intervall_list[-1]), x="TimeIntervall", y="MaxPower")
    fig = px.line(max_power_df, x="TimeIntervall", y="MaxPower")
    fig.update_xaxes(title_text='Time intervall [min]')
    fig.update_yaxes(title_text='Max Power [W]')

    # Festlegen der gewünschten Werte auf der x-Achse und y-Achse
    array_iL = np.array(intervall_list)/60

    desired_x_ticks = intervall_list # Werte der x-Achse als Liste
    desired_x_text = np.round(array_iL,1) # Texte der x-Achse als Liste (die Werte der x-Achse in Minuten)
    

    fig.update_layout(
        xaxis=dict(
            tickvals=desired_x_ticks,  # Die gewünschten Werte auf der x-Achse
            ticktext=desired_x_text   # Die Texte, die für diese Werte angezeigt werden sollen
        )
    )

    fig.show()


