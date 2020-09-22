import json

file = open('MOCK_DATA.json')
data = json.load(file)


def get_data():
    return data
