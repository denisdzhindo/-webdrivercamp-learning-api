def write_to_file(data, filename):
    with open('data.txt','w') as file:
        file.write(data)
    return(len(data))
    

if __name__ == "__main__":
    import os
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_name = f"{dir_path}/data.txt"

    data = """
    In the beginning the Universe was created. 
    This has made a lot of people very angry and been widely regarded as a bad move."""
    print(f"Files: {next(os.walk(dir_path), (None, None, []))[2]}")
    print()
    print(f"Number of char: {write_to_file(data, file_name)}")
    print(f"Files: {next(os.walk(dir_path), (None, None, []))[2]}")
    print()
    data = "Don't Panic"
    print(f"Number of char: {write_to_file(data, file_name)}")
    print(f"Files: {next(os.walk(dir_path), (None, None, []))[2]}")
