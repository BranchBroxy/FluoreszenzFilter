import importlib

import streamlit as st
import plotly.graph_objects as go
import plotly.io as pio
from plotly.subplots import make_subplots

import pandas as pd

from scipy.signal import find_peaks

import visutils
importlib.reload(visutils)




def main():

    df = pd.read_csv("Results_Calima_2021-12-06_neuro_Cal-520_dye-100_007.csv", index_col=0)

    st.dataframe(df)

    fig2 = make_subplots(rows=10, cols=1)

    figures = []

    for i, data in enumerate(df.iloc[:, 1:31]):
        peaks, _ = find_peaks(df[data], prominence=12)
        figures.append(go.Figure())

        figures[i].add_trace(go.Scatter(y=df[data], name=i+1, mode="lines"))
        figures[i].add_trace(go.Scatter(x=peaks, y=df[data][peaks], mode="markers", showlegend=True))

    for fig in figures:

        st.plotly_chart(fig)


if __name__ == "__main__":
    main()
