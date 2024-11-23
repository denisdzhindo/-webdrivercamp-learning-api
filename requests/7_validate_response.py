import json
import requests
from pprint import pprint

def find_mismatched_data(url, file_name):

    with open(file_name, 'r') as file:
        expected = json.load(file)
        expected_results = (expected.get("results", 0))

    r = requests.get(url)
    actual = r.json()
    actual_results = actual.get("results", 0)

    if len(actual_results) != len(expected_results): # check actual and expected lists length
        print(f"There are {len(actual_results)} planets, but expected {len(expected_results)}, please verify.")
        return

    result = dict()

    for actual, expected in zip(actual_results, expected_results):
        name = actual["name"]

        differences = []

        for key in actual:
            if key != 'name' and key in expected:
                if actual[key] != expected[key]:
                    diff = {key: {'actual': actual[key], 'expected': expected[key]}}
                    differences.append(diff)

        if differences:
            result[name] = differences

    return result

if __name__ == '__main__':

    my_url = 'https://swapi.dev/api/planets/'
    my_file = 'planets.json'
    pprint(find_mismatched_data(my_url, my_file))






