# Basic Syntax 
# type(file): <class '_io.TextIOWrapper'>
# file = open("./assets/users.txt")
# content = file.read()
# print(content)
# file.close()
#
# A file must always be closed after reading. Without closing:
# - memory leak
# - file lock
# - resource leak
#
# Returns "FileNotFoundError" if unable to read file or wrong path

# Recommended Python syntax:
#   with open(filePath) as file
# Python automatically closes the file.

filePath = "./assets/users.txt"

with open(filePath) as file:
    content = file.read()
print(content)

# "with" syntax internally, 
# file = open(...)
# try:
#     ...
# finally:
#     file.close()

# Because every line ends with "\n", we get extra blank
# line after every row. Hence use line.strip() to remove
# these extra lines.

# .strip() removes all leading/trailing whitespace, not just \n.
with open(filePath) as file:
    for line in file:
        print(line.strip())
    # for index, line in enumerate(file):
    #     print(f"Line {index+1}: {line.strip()}")

# readline() - Read only one line
# Need to call file.readline() function again
# to proceed to the next line
with open(filePath) as file:
    print("-- Readline --")
    print(file.readline())
    print("----")
    print(file.readline())

# readlines() - Returns a list.
with open(filePath) as file:
    lines = file.readlines()
# Result: 
# [
#     "Nishant\n",
#     "Rahul\n",
#     "Amit\n"
# ]
