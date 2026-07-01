# Program 8: Task Interleaving (Context Switching)
# Concept: Watching a single thread switch back and forth between two different workflows using create_task.
import asyncio
from time import time, ctime

async def kitchen_crew():
    print(f"{ctime()} -> Chef: putting spaghetti in boiling water...")
    await asyncio.sleep(1)  # Simulate a delay in cooking
    print(f"{ctime()} -> Chef: straining the noodles")

async def bar_crew():
    print(f"{ctime()} -> Bar Starts grinding coffee bean...")
    await asyncio.sleep(1)  # Simulate a delay in pouring
    print(f"{ctime()} -> Bar pours espresso shot")

async def main():
    start_time = time()
    task_kitchen = asyncio.create_task(kitchen_crew())
    task_bar = asyncio.create_task(bar_crew())

    await task_kitchen
    await task_bar

    print(f"Total Operation Time: {time() - start_time:.2f} seconds")  # Will be around 2 seconds
if __name__ == "__main__":
    
    asyncio.run(main())  # Run the main coroutine