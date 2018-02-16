import matplotlib.pyplot as plt
import pandas as pd

def storage_utilisation(df):
    # add the columns with the minimal, mean and max value of each day
    df["min"] = df.min(axis=1)
    df["mean"] = df.mean(axis=1)
    df["max"] = df.max(axis=1)


    df[['min','mean','max']].plot()
    axes = plt.gca()
    axes.set_ylim([0,1])

    plt.ylabel('storage utilisation rate')
    plt.xlabel('days')

    plt.show()
