# Objective: Extract returned data safely and inspect crashed tasks without breaking the main loop.

import asyncio
from time import ctime

async def division_worker(a, b):
    await asyncio.sleep(0.5)
    return a / b # 

async def main():
    task_success = asyncio.create_task(division_worker(10, 2))
    task_fail = asyncio.create_task(division_worker(10, 0))

    # รอคจนกว่า task ทั้งสองจะเสร็จสิ้น
    await asyncio.sleep(1)
    
    # ตอนที่ผ่านไป 1 วินาที มันเกิดอะไรขึ้น
    if task_success.done() and not task_success.exception():
        print(f"{ctime()} Task Success Result: {task_success.result()}") # คาดวหา task สำเร็จและได้ผลลัพธ์ 5
        
    # 
    if task_fail.done():
        print(f"{ctime()} Task Fail Exception: {type(task_fail.exception()).__name__}") # 

asyncio.run(main())