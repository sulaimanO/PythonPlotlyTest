import pandas as pd
import json
import csv
import numpy as np
from numpy import genfromtxt

file = pd.read_csv('MOCK_DATA.csv')
data = file.to_json(orient='records')

def get_data() -> object:
    return [file, data]


def csv_as_list():
    file = open("MOCK_DATA.csv")
    reader = csv.reader(file)
    records = list(reader)
    return records

def get_file_data():
    df = pd.read_csv('MOCK_DATA.csv', sep=',', header=None)
    return df.values