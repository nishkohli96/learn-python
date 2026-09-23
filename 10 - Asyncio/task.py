import asyncio


async def fetch_user():
    print("Fetching user...")
    await asyncio.sleep(2)
    print("User fetched")
    return "User"


async def main():
    task = asyncio.create_task(fetch_user())
    print("Task created")
    result = await task
    print(result)


asyncio.run(main())
