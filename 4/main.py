# import libraries
from read_pandas2 import read_activity_csv, find_best_effort, create_power_curve, make_plot_power_curve

# main
if __name__ == "__main__":
    df = read_activity_csv()
    best_power = find_best_effort(df, 30, 1)    
#------------------------------------------------------------
    intervall_list = [1, 30, 60, 120, 300, 600, 1200, 1800] # Zeitintervalle in Minuten 1s - 30min
    fs = 1 # Anzahl der Werte pro Sekunde
    max_power_df = create_power_curve(df, intervall_list, fs)
    print(max_power_df)

    make_plot_power_curve(max_power_df, intervall_list) # plot the power curve as interactive plot