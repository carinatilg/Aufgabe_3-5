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

with tab1:
    st.header("EKG-Data")
    st.write("# EKG-Data Plot")

    df = read_my_csv()
    fig = make_plot(df)

    st.plotly_chart(fig)

with tab2:
    st.header("Power-Data")
    st.write("# Power-Data Plot")

    df = read_activity_csv()
    fig2 = make_plotpower(df)

    st.plotly_chart(fig2)
    # app user-input
    eingabe = st.number_input("Maximale Herzfrequenz:")
    add_HR_zones(df, eingabe)
    # get time and power for each zone
    t_1, t_2, t_3, t_4, t_5 = compute_time_zones(df)
    p_1, p_2, p_3, p_4, p_5 = compute_power_in_zone(df)
    # print time and power for each zone
    st.write(t_1, "Sekunden in Zone 1, mit einer Leistung von", round(p_1,2), "Watt")
    st.write(t_2, "Sekunden in Zone 2, mit einer Leistung von", round(p_2,2), "Watt")  
    st.write(t_3, "Sekunden in Zone 3, mit einer Leistung von", round(p_3,2), "Watt")
    st.write(t_4, "Sekunden in Zone 4, mit einer Leistung von", round(p_4,2), "Watt")
    st.write(t_5, "Sekunden in Zone 5, mit einer Leistung von", round(p_5,2), "Watt")  
    
    