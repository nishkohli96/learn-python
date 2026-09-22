# Type Hints

Use **Pylance** or **Pyright** for type checking in python.

```bash
pip3 install pyright
```

## Any

When unsure about the type,

```py
from typing import Any

def process(data: Any):
    ...
```

`Any` basically says: Don't perform type checking here.

## Callable

`Callable` means: Something that can be called like a function.

```py
from collections.abc import Callable

Callable[[int], int]
```

means

```py
Callable[
    [argument types],
    return type
]
```

```py
from collections.abc import Callable

def execute(
    operation: Callable[[int], int],
    value: int
) -> int:
    return operation(value)
```

## TypeVar

Equivalent to "Generic" in Typescript.

```py
from typing import TypeVar

T = TypeVar("T")
def first(items: list[T]) -> T:
    return items[0]
```

```py
X = TypeVar("T")
```

`X` — this is the actual Python variable name you'll reference in your code (`list[X]`, `Generic[X]`, etc.). This is what matters for your code to run.
`"T"` — this is just a string label, passed as an argument to `TypeVar()`. It's used internally for error messages, `repr()`, and debugging — Python doesn't derive the variable name from this string; it's purely descriptive metadata.

Prefer using the same name to avoid confusion.

```py
Y = TypeVar("T")
print(Y)          # ~T   (the string "T", not "Y")
print(Y.__name__) # T

def add(a: Y, b: Y) -> Y:
    return a + b

add(1, "hello")
# error: Argument 2 has incompatible type "str"; expected "T"
# ^ says T, but you wrote Y everywhere in your code!
```

### Constrained TypeVar

Suppose,

```py
def double(value: int | float) -> int | float:
    return value * 2
```

If you give it an int, we'd like the result to remain int.

If you give it a float, we'd like the result to remain float.

We can use a constrained TypeVar:

```py
Number = TypeVar("Number", int, float)

def double(value: Number) -> Number:
    return value * 2
```

Conceptually Number can be `int` or `float`, but the input and output maintain the same generic type.

### Bounded TypeVar

Bounded TypeVar is a way to restrict a generic type parameter to only accept certain types (or their subtypes), rather than accepting literally anything.

```py
from typing import TypeVar

class Animal:
    def speak(self) -> str:
        return "..."

class Dog(Animal):
    def speak(self) -> str:
        return "Woof"

class Cat(Animal):
    def speak(self) -> str:
        return "Meow"

T = TypeVar("T", bound=Animal)   # T must be Animal OR any subclass of Animal

def make_speak(animal: T) -> T:
    print(animal.speak())
    return animal
```

`bound=Animal` means: whatever concrete type `T` ends up being for a given call, it must be `Animal` or a subtype of `Animal`. With the bound `TypeVar`, the type checker knows "whatever specific subtype went in, comes back out"

### Constrained vs Bound

| Concept | Meaning |
| - | - |
| `TypeVar("T")` | T can be literally any type |
| `TypeVar("T", bound=X)` | T must be `X` or a subtype of `X` — preserves the specific subtype through the function |
| `TypeVar("T", A, B)` | T must be exactly `A` or exactly `B` (constrained, not open to subclasses) |

**constraints** → choose from these types
**bound** → anything inside this type hierarchy

## Generic Classes

Generic is only needed for classes — to tell Python "this class is parameterized by T"

```py
from typing import Generic, TypeVar

T = TypeVar("T")

class Box(Generic[T]):
    def __init__(self, value: T):
        self.value = value

    def get(self) -> T:
        return self.value

number_box = Box(100)
string_box = Box("hello")
```

### Python 3.12+ - new syntax

```py
class Response[T]:
    data: T
    success: bool

def get_first[T](items: list[T]) -> T:
    return items[0]
```

## Protocol

Use Protocol when you're describing a capability/interface that many unrelated types might already satisfy — especially useful for things like "anything with a .read() method" (file-like objects), dependency injection, or typing third-party code you don't control.

"I don't care what class you are; I care whether you provide this behavior."

## Cheat Sheet

| Python                 | Purpose               | TypeScript equivalent    |
| ---------------------- | --------------------- | ------------------------ |
| `list[int]`            | List of ints          | `number[]`               |
| `dict[str, int]`       | Dict string → int     | `Record<string, number>` |
| `tuple[str, int]`      | Fixed tuple           | `[string, number]`       |
| `str \| None`          | String or None        | `string \| null`         |
| `str \| int`           | Multiple types        | `string \| number`       |
| `Any`                  | Disable type checking | `any`                    |
| `Callable[[int], str]` | Function type         | `(x: number) => string`  |
| `TypeVar`              | Generic type          | `<T>`                    |
| `TypedDict`            | Typed dictionary      | `interface`              |
| `Protocol`             | Structural interface  | `interface`              |
| `Literal`              | Fixed allowed values  | string literal union     |

```
                    GENERICS
                       │
          ┌────────────┴────────────┐
          │                         │
      TypeVar                    Generic
          │                         │
    Generic functions          Generic classes
          │                         │
          └────────────┬────────────┘
                       │
                  Type safety
                       │
          ┌────────────┴────────────┐
          │                         │
       Protocol                 TypedDict
          │                         │
    behavior-based             dict structure
```