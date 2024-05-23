import streamlit as st
from read_pandas import read_my_csv
from read_pandas import make_plot
from read_pandas import make_plotpower
from read_pandas import read_activity_csv
from read_pandas import add_HR_zones
from read_pandas import compute_time_zones
from read_pandas import compute_power_in_zone


# Wo startet sie Zeitreihe
# Wo endet sich
# Was ist die Maximale und Minimale Spannung
# Grafik
tab1, tab2 = st.tabs(["EKG-Data", "Power-Data"])

df = read_activity_csv()


with tab1:
    st.header("EKG-Data")
    st.write("# My Plot")

    df = read_my_csv()
    fig = make_plot(df)

    st.plotly_chart(fig)

with tab2:
    st.header("Power-Data")
    fig2 = make_plotpower(df)
    st.plotly_chart(fig2)
    eingabe = st.number_input("Maximale Herzfrequenz:")
    add_HR_zones(df, eingabe)
    t_1, t_2, t_3, t_4, t_5 = compute_time_zones(df)
    p_1, p_2, p_3, p_4, p_5 = compute_power_in_zone(df)

    st.write("Du warst",t_1, "Sekunden in Zone 1"
             "Du warst",t_2, "Sekunden in Zone 2"
             "Du warst",t_3, "Sekunden in Zone 3"
             "Du warst",t_4, "Sekunden in Zone 4"
             "Du warst",t_5, "Sekunden in Zone 5")
    
