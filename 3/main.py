import streamlit as st
from read_pandas import read_my_csv
from read_pandas import make_plot
from read_pandas import make_plotpower
from read_pandas import read_activity_csv


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