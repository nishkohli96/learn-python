# For more, refer Notes.md

from pathlib import Path

# p = Path("assets/users.txt")           # relative
# p = Path("/Users/nish/assets")         # absolute
# p = Path(__file__).resolve().parent    # anchor to current script's dir (from earlier)
# p = Path.cwd()                         # current working directory
# p = Path.home()                        # user's home directory

# # Joining paths — use /, not string concatenation:

# base = Path("assets")
# file_path = base / "students" / "data.csv"
# # assets/students/data.csv

p = Path("/Users/nish/assets/users.json")

print(p.name)        # 'users.json'
print(p.stem)        # 'users'          (filename without extension)
print(p.suffix)      # '.json'
print(p.suffixes)    # ['.json'] (or ['.tar', '.gz'] for 'file.tar.gz')
print(p.parent)      # /Users/nish/assets
print(p.parents[1])  # /Users/nish        (grandparent)
print(p.parts)       # ('/', 'Users', 'nish', 'assets', 'users.json')


# For p = Path("/Users/nish/assets"), the results would be:

# assets
# assets

# []
# /Users/nish
# /Users
# ('/', 'Users', 'nish', 'assets')
