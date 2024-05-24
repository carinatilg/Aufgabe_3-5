import pandas as pd
import numpy as np
import plotly.express as px


# Read Activity Data
def read_activity_csv():
    path = "../data/activities/activity.csv"
    df = pd.read_csv(path)

    return df


