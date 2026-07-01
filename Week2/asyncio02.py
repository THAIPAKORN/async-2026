# Program 2: The Coroutine Object
# Concept: Seeing that calling an async def function creates an "Object" but does not execute it yet.
import asyncio

async def greet():
    print("Hello!")

coro_object = greet()  # Calling the coroutine function creates a coroutine object
print(type(coro_object))  # Output: <class 'coroutine'>

coro_object.close()  # Closing the coroutine object to free resources