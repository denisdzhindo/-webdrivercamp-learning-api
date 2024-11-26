import json
import requests
from pprint import pprint

def find_mismatched_data(url, file_name):
    with open(file_name, 'r') as file:
        expected_data = json.load(file)
        expected_results = expected_data.get("results", [])

    r = requests.get(url)
    actual_data = r.json()
    actual_results = actual_data.get("results", [])

    if len(actual_results) != len(expected_results):
        print(f"There are {len(actual_results)} planets, but expected {len(expected_results)}. Please verify.")
        return

    mismatches = {}

    for actual, expected in zip(actual_results, expected_results):
        name = actual["name"] 
        differences = []

        for key, actual_value in actual.items():
            if key != 'name' and key in expected:
                expected_value = expected.get(key)
                if actual_value != expected_value:
                    differences.append({key: {'actual': actual_value, 'expected': expected_value}})

        if differences:
            mismatches[name] = differences

    return mismatches

if __name__ == '__main__':
    my_url = 'https://swapi.dev/api/planets/'
    my_file = 'planets.json'
    pprint(find_mismatched_data(my_url, my_file))


