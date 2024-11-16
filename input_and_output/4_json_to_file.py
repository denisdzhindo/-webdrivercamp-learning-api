import json

def to_json_file(file_name):
    data_object = {"list": [1, 2, 3, 4, 5],
                   "tuple": (1, 2, 3, 4, 5),
                   "string": "Hello World!",
                   "bool": False,
                   "null": None,
                   "int": 123,
                   "float": 3.14,
                   "dict": {"abc": True, "Hello": "World", 10: [2, 3, 4]}}
    
    with open("data.json","w") as file:
        json.dump(data_object, file, indent=4)

if __name__=="__main__":
    import os

    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_name = f"{dir_path}/data.json"
    
    to_json_file(file_name)

    with open(file_name, "r") as f:
        print(f.read())
