# Opening and closing a file

file = open('text_file.txt')
file.close()

file = open('text_file.txt')
try:
    # processing of data here
finally:
    file.close()

with open("text_file.txt") as file:
    # processing of data here






