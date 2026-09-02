# File Handling

## File Modes
| Mode   | Meaning                           |
| ------ | --------------------------------- |
| `"r"`  | Read (default)                    |
| `"w"`  | Write (creates or overwrites)     |
| `"a"`  | Append                            |
| `"x"`  | Create only if file doesn't exist |
| `"rb"` | Read binary                       |
| `"wb"` | Write binary                      |
| `"r+"` | Read and write                    |

Here's a deeper dive into each — building on everything covered so far.

## `pathlib.Path`

The modern, object-oriented way to handle filesystem paths (replaces most of `os.path`).

**Checking existence / type:**

```python
p.exists()      # True/False
p.is_file()
p.is_dir()
p.is_symlink()
```

Useful to replace `try/except FileNotFoundError` with an upfront check when that fits your flow better:

```python
if not p.exists():
    print(f"{p} not found.")
else:
    content = p.read_text()
```

**Reading/writing without a `with` block** — `Path` has these built in:

```python
text = p.read_text(encoding="utf-8")
p.write_text("hello", encoding="utf-8")

data = p.read_bytes()
p.write_bytes(b"...")
```

Handy for quick scripts; for anything needing explicit error handling around encoding/line-endings, `open()` in a `with` block still gives you more control.

**Creating directories/files:**

```python
p.mkdir()                        # fails if parent doesn't exist
p.mkdir(parents=True)            # create intermediate dirs too
p.mkdir(parents=True, exist_ok=True)  # don't error if it already exists

p.touch()                        # create empty file (like Unix `touch`)
p.touch(exist_ok=True)           # don't error if file exists
```

### Imports
```py
from pathlib import Path

# 1 dir up
one_up = Path(__file__).resolve().parent.parent

# 3 dirs up
three_up = Path(__file__).resolve().parent.parent.parent.parent
```

**Iterating a directory:**

```python
for item in Path("assets").iterdir():
    print(item, item.is_file())
```

**Globbing (pattern matching):**

```python
list(Path("assets").glob("*.csv"))        # all .csv files, this dir only
list(Path("assets").rglob("*.csv"))       # recursive, all subdirs too
list(Path(".").glob("**/*.py"))           # equivalent recursive pattern
```

**Renaming / deleting / moving:**

```python
p.rename("new_name.txt")     # rename/move
p.unlink()                   # delete a file
p.unlink(missing_ok=True)    # don't error if it doesn't exist (3.8+)
p.rmdir()                    # delete an empty directory
```

**Comparisons and equality** — `Path` objects compare by their string path, so you can use them directly in sets/dicts or with `==`:

```python
Path("a/b") == Path("a") / "b"   # True
```

**Quick contrast — old `os.path` vs `pathlib`:**

| Task | `os.path` | `pathlib` |
|---|---|---|
| Join paths | `os.path.join(a, b)` | `a / b` |
| File exists | `os.path.exists(p)` | `p.exists()` |
| Get filename | `os.path.basename(p)` | `p.name` |
| Get extension | `os.path.splitext(p)[1]` | `p.suffix` |
| Absolute path | `os.path.abspath(p)` | `p.resolve()` |

## `json`

**Core functions — note the naming pattern (`load`/`dump` = files, `loads`/`dumps` = strings):**

```python
import json

json.load(file_obj)     # read JSON from an open file → Python object
json.dump(obj, file_obj) # write Python object → JSON, to an open file
json.loads(str)          # parse a JSON string → Python object
json.dumps(obj)          # convert Python object → JSON string
```

**Type mapping (Python ↔ JSON):**

| Python | JSON |
|---|---|
| `dict` | object |
| `list`, `tuple` | array |
| `str` | string |
| `int`, `float` | number |
| `True`/`False` | `true`/`false` |
| `None` | `null` |

Note: `tuple` becomes a JSON array on the way out, but comes back as a `list` on the way in — round-tripping isn't perfectly symmetric.

**Pretty-printing with `dumps`/`dump`:**

```python
user = {"name": "Nishant", "age": 30, "city": "Bengaluru"}

print(json.dumps(user, indent=2))
# {
#   "name": "Nishant",
#   "age": 30,
#   "city": "Bengaluru"
# }

print(json.dumps(user, indent=2, sort_keys=True))  # alphabetical keys
```

**Compact output** (useful for network payloads, minimizing size):

```python
json.dumps(user, separators=(',', ':'))
# {"name":"Nishant","age":30,"city":"Bengaluru"}
```

**Non-ASCII characters:**

```python
data = {"city": "Bengaluru", "note": "café"}
json.dumps(data)                        # '{"city": "Bengaluru", "note": "caf\u00e9"}'
json.dumps(data, ensure_ascii=False)    # '{"city": "Bengaluru", "note": "café"}'
```

By default, `ensure_ascii=True` escapes all non-ASCII into `\uXXXX` sequences — still valid JSON, just not human-readable. Set `False` if you want actual UTF-8 characters in the output.

**Serializing objects `json` doesn't know how to handle** — e.g. `datetime`:

```python
from datetime import datetime

data = {"created": datetime.now()}
json.dumps(data)
# TypeError: Object of type datetime is not JSON serializable
```

Fix with a custom `default` function, called for any type `json` can't natively convert:

```python
def custom_serializer(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()
    raise TypeError(f"Type {type(obj)} not serializable")

json.dumps(data, default=custom_serializer)
# '{"created": "2026-08-10T14:32:10.123456"}'
```

**Custom decoding** — turning JSON back into a specific Python type (e.g. dicts back into a class instance), via `object_hook`:

```python
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __repr__(self):
        return f"User({self.name}, {self.age})"

def as_user(dct):
    if "name" in dct and "age" in dct:
        return User(dct["name"], dct["age"])
    return dct

json.loads('{"name": "Nishant", "age": 30}', object_hook=as_user)
# User(Nishant, 30)
```

**Error handling recap (from earlier) — `json.JSONDecodeError`:**

```python
try:
    data = json.loads(some_string)
except json.JSONDecodeError as e:
    print(e.msg, e.lineno, e.colno, e.pos)  # exact failure location
```

## `csv`

**Basic reader/writer** (already covered) — here's more control over both.

**`DictReader` / `DictWriter`** — work with rows as dicts instead of positional lists, keyed by the header row. Much less fragile than `row[0]`, `row[1]`:

```python
import csv

with open("students.csv", newline='') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["name"], row["age"])
        # row is an OrderedDict/dict: {'name': 'Alice', 'age': '15', 'grade': 'A'}
```

```python
with open("students.csv", "w", newline='') as file:
    fieldnames = ["name", "age", "grade"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({"name": "Alice", "age": 15, "grade": "A"})
    writer.writerows([
        {"name": "Bob", "age": 16, "grade": "B"},
        {"name": "Amy", "age": 17, "grade": "A"},
    ])
```

**Plain `writer` (list-based):**

```python
with open("out.csv", "w", newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["name", "age"])
    writer.writerows([["Alice", 15], ["Bob", 16]])
```

Always pass `newline=''` when *writing* too — otherwise on Windows you get doubled blank lines between rows, because both `csv.writer` and the text-mode file translation each add line endings.

**Dialects & delimiters** — not every "CSV" uses commas:

```python
# Tab-separated
reader = csv.reader(file, delimiter='\t')

# Semicolon-separated (common in European locales/Excel exports)
reader = csv.reader(file, delimiter=';')

# Custom quote character
reader = csv.reader(file, quotechar="'")
```

**Quoting control on write** — how aggressively to wrap fields in quotes:

```python
csv.writer(file, quoting=csv.QUOTE_MINIMAL)   # default: quote only if needed (has comma, quote, newline)
csv.writer(file, quoting=csv.QUOTE_ALL)       # quote every field
csv.writer(file, quoting=csv.QUOTE_NONNUMERIC) # quote all non-numeric fields
csv.writer(file, quoting=csv.QUOTE_NONE)      # never quote (raises error if a field needs it, unless escapechar set)
```

**Auto-detecting the format of an unfamiliar CSV** — `csv.Sniffer`:

```python
with open("mystery.csv", newline='') as file:
    sample = file.read(2048)
    file.seek(0)  # rewind after sampling

    dialect = csv.Sniffer().sniff(sample)
    has_header = csv.Sniffer().has_header(sample)

    reader = csv.reader(file, dialect)
    if has_header:
        next(reader)  # skip header row
    for row in reader:
        print(row)
```

Useful when you're ingesting CSVs from unknown/varied sources (some use `,`, some `;`, some `\t`) and don't want to hardcode the delimiter.

**Registering a custom dialect** (if you reuse the same non-standard format often):

```python
csv.register_dialect('pipes', delimiter='|', quoting=csv.QUOTE_MINIMAL)

with open("data.psv", newline='') as file:
    reader = csv.reader(file, dialect='pipes')
```

**Combining with `pathlib`** (tying it all together):

```python
from pathlib import Path
import csv

csv_path = Path(__file__).resolve().parent / "assets" / "students.csv"

if csv_path.exists():
    with csv_path.open(newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        students = list(reader)
    print(students)
else:
    print(f"{csv_path} not found.")
```

Note `csv_path.open(...)` — `Path` objects have an `.open()` method equivalent to the builtin `open(csv_path, ...)`, so you rarely need to convert back to a string.
