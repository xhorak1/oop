# import os

def write_to_file(file_name, data):
    with open(file_name, "w") as file_handler:
        file_handler.write(data)

def read_from_file(file_name):
    data = None
    with open(file_name, "r") as file_handler:
        data = file_handler.read()

    return data


if __name__ == '__main__':
    MY_FILE = "file.txt"

    user_input = input("Zadej zprávu: ")
    write_to_file(MY_FILE, user_input)
    print("Zápis se povedl")

    data = read_from_file(MY_FILE)
    print(data)