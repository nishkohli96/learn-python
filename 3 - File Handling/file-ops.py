from pathlib import Path

# Directory this script lives in
BASE_DIR = Path(__file__).resolve().parent
print('Path(__file__).resolve(): ', Path(__file__).resolve())
# /Users/nish/coding/python/learn/3 - File Handling/file-ops.py

file_path = BASE_DIR / "../assets/users.txt"

write_filePath = "./assets/abc.txt"
read_write_file = "./assets/hello.txt"

# This overwrites the file content
# with open(filePath, "w") as file:
#     file.write("Hello")

# Recommended: Append
with open(file_path, "a") as file:
    file.write("\nTom")

# Creating a file
# If file exists -> FileExistsError
# open("users.txt", "x")

# Writing to a file, creates if file doesn't exist
# Can write single or multiple lines
with open(write_filePath, "w") as file:
    file.write("A\n")
    file.write("B\n")
    file.write("C\n")

# File Pointer - Python remembers where you are.
# Python continues from where it stopped.
with open(read_write_file) as file:
    print(file.read(2))  # He
    print(file.read(2))  # ll
    # Where am I? Returns current position.
    print("File pointer is at: ",file.tell()) #4

# file.seek(0) -> Move pointer back to start
