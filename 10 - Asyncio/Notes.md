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

JavaScript              Python
────────────────────────────────────
Promise                 Coroutine
async function          async def
await                   await
Promise.all()           asyncio.gather()
setTimeout / timers     asyncio.sleep()
Event loop              Event loop