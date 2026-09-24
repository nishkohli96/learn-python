# AsyncIO

`asyncio` primarily provides concurrency, not CPU parallelism. Basic syntax:

```py
import asyncio

async def fetch_data():
    print("Fetching...")
    await asyncio.sleep(2)
    print("Done")

result = fetch_data()
```

**An async def doesn't immediately execute**.

`fetch_data()` produces a **coroutine object**. Conceptually:

```py
greet()
   ↓
Coroutine object
   ↓
needs to be awaited/run
```

You can run it with:

```py
asyncio.run(greet())
```

`asyncio.run()` creates/runs the event loop and executes the **coroutine**.

## asyncio.sleep vs time.sleep

```py
import time

time.sleep(2)
await asyncio.sleep(2)
```

`time.sleep()` blocks the thread. `asyncio.sleep()` essentially says: "I'm waiting. Let other async tasks run while I'm waiting."

## asyncio.gather()

`asyncio.gather()` Is Similar to `Promise.all()`

```py
import asyncio


async def task_a():
    print("A started")
    await asyncio.sleep(3)
    print("A finished")


async def task_b():
    print("B started")
    await asyncio.sleep(1)
    print("B finished")


async def main():
    await asyncio.gather(
        task_a(),
        task_b(),
        return_exceptions=True
    )


asyncio.run(main())
```

Without `return_exceptions`, if one task raises an exception, `gather()` propagates that exception, so that exception would be raised instead.

With `return_exceptions=True` you would get something like:

```py
[
    ValueError("A failed"),
    "B completed"
]
```

> asyncio.run() expects a coroutine, but asyncio.gather() returns a Future-like awaitable, not a coroutine.
>
> So you should put gather() inside an async function

If we were to write,

```py
await task_a()
await task_b()
```

It Doesn't automatically mean multiple tasks run concurrently, it is still sequential.

### Real World Example

```py
user, orders, recommendations = await asyncio.gather(
  get_user(),
  get_orders(),
  get_recommendations()
)
```

### Analogy with Javascript

| JavaScript | Python |
| - | - |
| Promise | Coroutine |
| async function | async def |
| await | await |
| Promise.all() | asyncio.gather() |
| setTimeout / timers | asyncio.sleep() |
| Event loop | Event loop |

## Task

```py
async def fetch_user():
    await asyncio.sleep(2)
    return "User"

coro = fetch_user()
```

When you call `fetch_user()` you get a coroutine object. At this point, the coroutine hasn't necessarily been scheduled to run.

**A Task is a coroutine that has been scheduled to run by the event loop.**

```py
async def fetch_user()
        ↓
   fetch_user()
        ↓
    Coroutine
        ↓
asyncio.create_task()
        ↓
      Task
        ↓
 Event loop schedules it
```

### Why Do We Need `create_task()`?

Think of `create_task()` as "Start This in the Background. I'll decide when to wait for its result."

It is conceptually somewhat similar to starting an async operation in Node.js and keeping its promise/future around.

Consider:

```py
async def main():
    user = await fetch_user()
    orders = await fetch_orders()
```

This is sequential:

```
fetch_user
    ↓
wait
    ↓
finish
    ↓
fetch_orders
    ↓
wait
    ↓
finish
```

But we can schedule both immediately:

```py
async def main():
    user_task = asyncio.create_task(fetch_user())
    orders_task = asyncio.create_task(fetch_orders())

    user = await user_task
    orders = await orders_task
```

Now:

```
create user task ────────┐
                         │
create orders task ──────┤
                         ↓
                  Event Loop
                  runs both
```

They can make progress concurrently.

### `create_task()` vs `gather()`

`gather()`:

```py
results = await asyncio.gather(
    fetch_user(),
    fetch_orders()
)
```

is convenient when you simply want:

**"Run these things concurrently and give me their results."**

`create_task()`

```py
user_task = asyncio.create_task(fetch_user())
orders_task = asyncio.create_task(fetch_orders())
```

is useful when you want to create/schedule the tasks now and await them later.

For example:

```py
async def main():

    user_task = asyncio.create_task(fetch_user())
    orders_task = asyncio.create_task(fetch_orders())

    print("Tasks are running...")

    user = await user_task
    orders = await orders_task
```

## Mental Mode

```
                 EVENT LOOP
                     │
             "Who can run?"
                     │
        ┌────────────┼────────────┐
        ↓            ↓            ↓
      Task A       Task B       Task C
        │            │            │
      await        await        await
        │            │            │
        ↓            ↓            ↓
     waiting      waiting      ready
                                  │
                                  ↓
                              RUN TASK
                                  │
                                await
                                  │
                                  ↓
                         back to event loop
```

## asyncio.to_thread()

`to_thread()` is for synchronous blocking functions.

This is particularly useful when you have:
- legacy synchronous code
- blocking SDKs
- synchronous file operations
- CPU-light but blocking functions
- third-party libraries without async support

For example:

```py
result = await asyncio.to_thread(sync_function)
```

Think: "Run this blocking synchronous function in a separate thread and give me the result asynchronously."

But don't use `to_thread()` for everything!

```py
def fetch_from_legacy_api(user_id, timeout):
    time.sleep(3)
    return {
        "user_id": user_id,
        "timeout": timeout,
        "status": "success"
    }

result = await asyncio.to_thread(
    fetch_from_legacy_api,
    123,
    10
)
```
