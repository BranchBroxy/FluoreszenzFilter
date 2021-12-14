import math
import pandas as pd
import numpy as np
from scipy.signal import find_peaks
import matplotlib.pyplot as plt

def use_filter(a, b, c):

    df = pd.read_csv("Results_2021-12-01_neuro_Cal-520_shorty-300s_mcor_Calima.csv")
    frames = df.shape[0]
    safer = np.zeros(shape=(frames, 1))
    for i, row in enumerate(df.iloc[:, 1:31]):
        for x, coloum in enumerate(df.iloc[:, i+1]):

            y = a * math.exp(-b * x) + c
            safer[x] = coloum - y
            print(y)
            print("he")
    #     peaks, _ = find_peaks(df[data], prominence=12)

    plt.plot(safer)
    plt.show()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    use_filter(7.69989, 0.00069002, 109.20678)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
