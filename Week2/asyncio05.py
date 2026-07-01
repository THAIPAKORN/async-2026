# Program 5: Sequential Execution (The Wrong Way)
# Concept: Showing that simply awaiting one after another is still sequential (Synchronous behavior).
import asyncio
from time import time,ctime

async def sever_cistomer(name):
    print(f"[{ctime()}] Cooking for {name}")
    await asyncio.sleep(1)
    print(f"{ctime()} Server for {name}")

async def main():
    start = time()

    await sever_cistomer("A")
    await sever_cistomer("B")

    print(f"Total time: {time() - start:.2f} seconds")


if __name__ == "__main__":
    asyncio.run(main())  # Running the main coroutine