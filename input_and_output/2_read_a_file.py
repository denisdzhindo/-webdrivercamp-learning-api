def read_a_file(filename):
    with open(filename, "r") as file:
        lines =file.readlines()
    line_number = 2
    if line_number < len(lines):
        print(lines[line_number])
    else:
        print("Line number is out of range")

if __name__ == "__main__":
    import os
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_name = f"{dir_path}/data.txt"

    read_a_file(file_name)


