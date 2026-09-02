# Iterators and Generators

## Iterable & Iterator

**Iterable**: Something you can loop over. Eg: `list`, `tuple`, `dictionary`, `range`.

```py
for number in numbers:
    print(number)
```
is equivalent to

```py
iterator = iter(numbers)

while True:
    try:
        number = next(iterator)
        print(number)
    except StopIteration:
        break
```

### Iterable vs Iterator

Iterable -> Can give you an iterator.

```py
numbers = [1, 2, 3]

iter(numbers)
```

Iterator -> Produces the next value.

```py
iterator = iter(numbers)

next(iterator)
```

> A useful way to remember:
>
> Iterable = something you can iterate over.
> Iterator = the object that actually remembers where you are during iteration.

### Custom Iterators

Python allows you to create your own iterator. You need two methods:

```py
__iter__()
__next__()
```

## Generator

**A generator is a simple way to create an iterator.**

Instead of:

```py
__iter__()
__next__()
StopIteration
```

you can use: `yield`.

### yield vs return

The core difference: `return` **exits the function completely** and hands back one final value. `yield` **pauses the function**, hands back one value, and remembers exactly where it left off — so it can resume from that exact point next time.

```py
def get_numbers():
    return [1, 2, 3]

result = get_numbers()
print(result)   # [1, 2, 3]
```

Once `return` executes, the function's work is over. Call it again, and it starts from scratch, top to bottom.

`yield` — function pauses, becomes a generator.

The moment a function contains any `yield`, it's no longer a normal function — calling it doesn't run the code at all. It returns a generator object, and the code only actually runs when you pull values from it (via `next()` or a `for` loop).

```py
def get_numbers():
    yield 1
    yield 2
    yield 3

gen = get_numbers()
print(gen)          # <generator object get_numbers at 0x...>  - nothing has run yet!

print(next(gen))    # 1  - runs up to first yield, pauses
print(next(gen))    # 2  - resumes right after last yield, runs to next one, pauses
print(next(gen))    # 3
print(next(gen))    # StopIteration - function actually finishes (falls off the end)
```

Why use `yield` over `return` [...] - the real payoff: memory efficiency.With yield, values are produced lazily — one at a time, only as you ask for the next one — instead of computing and storing everything upfront.

### Generator Expressions

Just as you have list comprehensions:
```py
squares = [x * x for x in range(10)]
```

you can create a generator expression.
```py
squares = (x * x for x in range(10))
```

Produces values lazily. You can do:
```py
print(next(squares)) # 0
print(next(squares)) # 1
print(next(squares)) # 4
```

### List vs Generator

|                         | List       | Generator             |
| ----------------------- | ---------- | --------------------- |
| Evaluation              | Immediate  | Lazy                  |
| Memory                  | Higher     | Usually much lower    |
| Can reuse directly      | Yes        | No, usually exhausted |
| Indexing                | Yes        | No                    |
| `len()`                 | Yes        | No                    |
| `next()`                | No         | Yes                   |
| Good for huge sequences | Not always | Yes                   |

## Relations

```
ITERABLE
   │
   │ iter()
   ↓
ITERATOR
   │
   │ next()
   ↓
VALUE
   │
   │ next()
   ↓
VALUE
   │
   │ next()
   ↓
VALUE
   │
   ↓
StopIteration
```

```
Generator function
       │
       │ yield
       ↓
   Generator
       │
       │ next()
       ↓
    value
       │
       │ next()
       ↓
    value
```
