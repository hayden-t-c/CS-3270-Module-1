"""
Module 1 is an introduction to the system.
It demonstrates how to set up a Python environment.

Hayden Christenson
6 September 2025
"""
import csv
import pandas as pd

def loadCSV(filepath):
    """
    This function loads a csv file into a pandas dataframe.
    Function returns that pandas dataframe.
    """
    csvdata = pd.read_csv(filepath)
    return csvdata

if __name__ == '__main__':
    data = loadCSV("Weather Data/Weather Training Data.csv")
    print("Pandas Method", len(data))
    print(data.describe())