# service to get all the general data

import repository as repo
import pandas as pd
import numpy as np
import json


def get_table_of_all_data():
    return repo.get_data()


def get_data_without_id_and_index():
    df = repo.get_data()[0]
    df.reset_index(drop=True, inplace=True)
    # delete column
    del df['id']
    return df


# total particpint,
def general_numbers():
    total_records = len(repo.csv_as_list())
    total_countries = get_countries()[0]
    total_females = get_male_and_female()[1]
    total_males = get_male_and_female()[3]

    return [total_records - 1, total_countries, total_females, total_males]


def get_countries():
    array = np.asarray(repo.csv_as_list())
    countries = []
    # get array of countries
    for record in array:
        country = record[3]
        countries.append(country)

    # unique values only
    countries_set = set(countries)
    countries_list = list(countries_set)
    countries_len = len(countries_set)

    return [countries_len - 1, countries_list]


def get_male_and_female():
    array = np.asarray(repo.csv_as_list())
    female = []
    male = []

    for record in array[1:]:
        gander = record[2]
        if gander == 'Female':
            female.append(record)
        else:
            male.append(record)

    female_len = len(set(map(tuple, female)))
    male_len = len(set(map(tuple, male)))

    return [female, female_len, male, male_len]
