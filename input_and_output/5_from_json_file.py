import json

def from_json_file(file):
    with open(file) as f:
        data = json.load(f)
    return data

if __name__=="__main__":
    import os
    
    dir_path = os.path.dirname(os.path.realpath(__file__))
    my_file_name = f"{dir_path}/data.json"
    
    data_object = from_json_file(my_file_name)

    print(data_object)
    print(type(data_object))
    print()
    for key, val in data_object.items():
        print(f"{key}: {type(val).__name__}")
                    







    
                    



