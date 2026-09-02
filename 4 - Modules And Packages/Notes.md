# Modules & Packages

## Module
A module is simply a Python file (`.py`) containing Python code.

### Import Syntax

1. Full Import
  Eg: `import math_utils` in `main.py`

2. Import Specific functions
  Eg: `from math_utils import add, subtract`

	Avoid `from math_utils import *`, as it makes it unclear,
	from which module a particular function came from.

3. Alias Imports
  ```py
	import pandas as pd
	pd.DataFrame(...)
	```

### Module Name

Every Python module has a special variable: `__name__`

If you print `__name__` in the module itself, it will always return `__main__`.

But if another file imports it:

```py
import calculator
```

then inside `calculator.py`, print(__name__) outputs `calculator`

### if __name__ == "__main__"

```py
def add(a, b):
    return a + b

if __name__ == "__main__":
    print(add(10, 20))
```

If I run - `python calculator.py`, it prints `30`, but if another file imports it,

The following won't execute:

`if __name__ == "__main__":`

because

`calculator.__name__ == "calculator"`

## Package

A package is a directory containing Python modules.

Example:

```
myapp/
│
├── main.py
│
└── utils/
    ├── __init__.py
    ├── math.py
    └── string.py
```

Here `utils` is a package and `math` and `string` are modules.

### Importing from a Package

Suppose `utils/math.py` contains `add` function. Then,

```py
from utils.math import add
print(add(10, 20))
```

OR

```py
import utils.math
print(utils.math.add(10, 20))
```

### __init__.py

`__init__.py` tells Python: "This directory should be treated as a package."

It can also contain initialization code or expose selected functionality.

```py
# utils/__init__.py

from .math import add
```

Now you may be able to do: - `from utils import add`

Modern Python also supports namespace packages without `__init__.py`, but you'll still encounter `__init__.py` constantly in real projects and should understand it.

### Relative Imports

Inside a package, you may see:

`from .math import add`

- `.`: means current package/directory.
- `..`: means go up one package level.
  ```py
	from ..utils import something
	```

Say if a module is 4 folders below the `__init__.py`,

```py
# 4 levels down, still one leading dot
from .sub1.sub2.sub3.sub4.module import do_thing
```

Absolute import (works the same from anywhere, as long as mypackage itself is importable — installed, or its parent dir is on sys.path).

In the traditional (and most common) setup, every folder in that chain needs its own `__init__.py`, not just the top-level mypackage and the final sub4.

```py
from mypackage.sub1.sub2.sub3.sub4.module import do_thing
```

**Common pitfalls:**

1. Relative imports only work when the file is part of a package being imported, not when run directly as a script:
2. Missing __init__.py in an intermediate folder — breaks the whole chain silently with ModuleNotFoundError: No module named 'mypackage.sub1.sub2'
3. Namespace packages (no `__init__.py` at all) — Python **3.3+** allows folders without `__init__.py` to still act as packages ("implicit namespace packages"). This works too, but is generally used for specific plugin/distributed-package scenarios rather than a normal single-project layout — if you're just organizing your own code, explicit `__init__.py` files (even empty) are the more predictable, conventional choice.

## pip

To ensure it is installed, check
`python3 -m pip --version`

### Add pip to path

```bash
echo 'export PATH="$HOME/Library/Python/3.14/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

For Mac, it is `pip3` just like `python3`.

### Auto update pip

```bash
pip3 install --upgrade pip
```

### pip install

`pip3` install default → global site-packages (system-wide), not per-project. Unlike `node_modules`, Python no auto per-project isolate.

fix: use virtual env (venv), scoped to project folder, like `node_modules`.

| Operation | Command |
|-|-|
| Install Pkg (latest version) | `pip3 install requests` |
| Install a specific version | `pip install requests==2.32.4` |
| Upgrade | `pip install --upgrade requests` |
| Uninstall | `pip uninstall requests` |
| List installed packages | `pip list` |


## Virtual Environments

If you have, say Django 5 installed on your system, but a project needs Django 4, we need to create a virtual environment for this project.

```bash
python3 -m venv .venv
```

```
python3   -m        venv     venv
  |        |          |        |
interpreter  |    module name  |
        "run a module"      argument (your custom folder name)
```
```
my-project/
│
├── .venv/
├── main.py
└── requirements.txt
```

The `.venv` contains the project's isolated Python environment.
It should be added to `.gitignore` as `venv/`

### Multiple venv

Can you have 2 venv folders for one project?

Yes, absolutely — for the following reasons:
- Testing against different Python versions:
```bash
python3.10 -m venv venv310
python3.12 -m venv venv312
```
- Separate dev vs. production dependency sets
- A monorepo with multiple sub-projects, each needing its own isolated deps — one venv per sub-folder.

**Important caveat: only one venv can be activated at a time in a given shell session.**

```bash
source venv-dev/bin/activate
# ... work ...
deactivate

source venv-prod/bin/activate
# ... different set of installed packages now active ...
```

In this case, multiple `requirements.txt` can be created.

### Activating Virtual Environment

**Mac/Linux**

```bash
source .venv/bin/activate
```

**Windows**

```bash
.venv\Scripts\activate
```

You'll usually see something like: `(.venv) $`.

> You must activate venv after creating it.
>
> Once active, your shell prompt usually shows (venv) prefixed, and pip install X now installs into this folder only — not globally:
>
> `(venv) nish@Nishants-MacBook-Air sample-app`
>
> On running `which python` after activating, you will see that it should point inside venv/bin/python, not the global one.

Any package you install now should go under:
`{project-name}/venv/lib/python3.14/site-packages`

Run `deactivate` to deactivate the virtual environment.

## requirements.txt

Suppose your project uses - `requests`, `pandas`, `flask`

You can save dependencies:
`pip freeze > requirements.txt`

You'll get something like:

```
Flask==3.x.x
pandas==2.x.x
requests==2.x.x
```

Another developer can install everything with:

```bash
pip install -r requirements.txt
```

### Format

```
requests==2.31.0
flask>=2.0,<3.0
numpy
pandas==2.1.4
```

- `==` pins an exact version (most reproducible, common for apps).
- `>=`, `<=`, `<`, `>` set version ranges.
- No version specifier at all → installs whatever the latest available version is (least reproducible — risky for teams/production).

Generating it from your current environment (after you've pip installed what you need):

```bash
pip freeze > requirements.txt
```

`pip freeze` dumps every installed package with its exact version — this is why you do it inside an activated venv, not globally, otherwise you'll dump every package on your entire system into the file.

`requirements.txt` will also contain **transitive dependencies** - packages which other pages depend upon.

### Install packages from a repo

Installing from it (what a teammate, CI server, or future-you runs):
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Typical Flow

```bash
# Start a new project
mkdir myproject && cd myproject
python3 -m venv venv
source venv/bin/activate

# Install what you need
pip install requests flask

# Freeze it for others / for later
pip freeze > requirements.txt

# .gitignore
echo "venv/" >> .gitignore

# --- later, or on another machine ---
git clone <repo>
cd myproject
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt   # exact same packages, reproduced
```

### For multiple venv

**Pattern 1: Dev vs. Prod (most common)**

```bash
# Production venv
python3 -m venv venv-prod
source venv-prod/bin/activate
pip install -r requirements.txt

# Dev venv
python3 -m venv venv-dev
source venv-dev/bin/activate
pip install -r requirements-dev.txt   # pulls in requirements.txt too, plus dev tools
```

**Pattern 2: Multiple Python versions (testing compatibility)**

Here you usually want the same `requirements.txt`, just installed into separately-versioned venvs — no need for separate files, since the packages you want are identical, only the interpreter differs:

```bash
python3.10 -m venv venv310 && venv310/bin/pip install -r requirements.txt
python3.12 -m venv venv312 && venv312/bin/pip install -r requirements.txt
```

**Pattern 3: Monorepo, independent sub-projects**

Each sub-project gets its own `requirements.txt` at its own root — these are genuinely separate projects, so no shared/layered file makes sense:

```
backend/
    venv/
    requirements.txt
frontend-api/
    venv/
    requirements.txt
```

Each is generated and maintained independently (pip freeze > requirements.txt inside its own activated venv).

Common file-naming convention across teams:
| File | Purpose |
| - | - |
|`requirements.txt` |	Core/production deps |
|`requirements-dev.txt` |	Adds dev tools (linters, formatters, test runners) |
|`requirements-test.txt` |	Testing-only deps (pytest, coverage tools) — sometimes split further from dev |
|`requirements-docs.txt` | Docs-building deps (Sphinx, mkdocs) |

All of these typically -r `requirements.txt` at the top to avoid duplicating the base list.

Recommended way is to list core dependencies in `requirements.txt`, and then in say, 
`requirements-dev.txt` you chain `requirements.txt` and add the dev tools for that venv.

```bash
# requirements-dev.txt
-r requirements.txt
pytest==8.3.0
black==24.10.0
mypy==1.13.0
```

So when I do `pip3 install -r requirements-dev.txt`, it will install dependencies from `requirements.txt` as well as the additional dependencies listed in `requirements-dev.txt`.
