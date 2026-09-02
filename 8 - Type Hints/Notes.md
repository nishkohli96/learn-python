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
