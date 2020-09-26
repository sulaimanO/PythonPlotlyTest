# service to get all the general data

import repository as repo
import pandas as pd
import numpy as np


def get_table_of_all_data():
    return repo.get_data()


def get_data_without_id_and_index():
    df = repo.get_data()[0]
    df.reset_index(drop=True, inplace=True)
    # delete column
    del df['id']
    return df

def general_numbers():
    total_records = len(repo.csv_as_list())
    print(total_records)

    array = np.asarray(repo.csv_as_list())

    countries = []
    male = []
    female = []

    for record in array:
        countries.append(record[3])

