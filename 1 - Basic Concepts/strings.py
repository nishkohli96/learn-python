print("\\\"Hello World'!")

long_string = """This is a long string!
This is next line of this long string.
"""
print(long_string)

some_string = "This string \nbreaks in new line"
print(some_string)

spaced_string = " THis string has spacing at start & end. "
# Removes whitespaces from the beginning and ending of the string.
# ".lstrip" to remove space from start, and ".rstrip" to remove space from end
print(spaced_string.strip())

course_name = "python programming"
# f("") is template variable -> similar to `${var}` in JS
# len(str) is to get length of a string
print(f"length of some_string: {len(course_name)}")
print(f"capitalize: {course_name.capitalize()}")
print(f"upper: {course_name.upper()}")
print(f"lower: {course_name.lower()}")
print(f"title: {course_name.title()}")

# Index '0' gives first char of the string, while '-1' gives
# the last char of string.
print(f"course_name[0]: {course_name[0]}")

# Equivalent to JS str.slice(), end index is not included
print(f"course_name[3:7]: {course_name[3:7]}")
# Prints till the end of the string
print(f"course_name[3:]: {course_name[3:]}")
# Returns copy of the original string
print(f"course_name[:]: {course_name[:]}")

# Returns starting index of substring; returns -1 if not found
print(f"index of \"pro\" in course_name: {course_name.find("pro")}")

print(f"replace of \"p\" by \"J\" in course_name: {course_name.replace("p", "J")}")

# Check if a string contains a substr.
# "pro" not in course_name -> returns False
print("is \"pro\" in course_name", "pro" in course_name)
