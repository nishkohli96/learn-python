import asyncio


async def greet():
    print("Hello")
    await asyncio.sleep(2)
    print("Goodbye")


asyncio.run(greet())


async def task_a():
    print("A started")
    await asyncio.sleep(3)
    print("A finished")


async def task_b():
    print("B started")
    await asyncio.sleep(1)
    print("B finished")


async def main():
    await asyncio.gather(task_a(), task_b())


asyncio.run(main())


async def fetch_user():
    await asyncio.sleep(2)
    return "User"


async def fetch_orders():
    await asyncio.sleep(3)
    return "Orders"


async def fetch_recommendations():
    await asyncio.sleep(1)
    return "Recommendations"


async def api_main():
    # With `return_exceptions=True` you would get exception value
    # in the respective result var. Without it, only the exception
    # would be raised and the program crashes.
    users, orders, recommendations = await asyncio.gather(
        fetch_user(),
        fetch_orders(),
        fetch_recommendations(),
        return_exceptions = True
    )
    # Unlike JS, you canntot use a object-property shorthand syntax,
    # as the result would yield in a "set", not a dictionary. 
    return {"users": users, "orders": orders, "recommendations": recommendations}


print(asyncio.run(api_main()))
