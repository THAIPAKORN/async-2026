# Objective: Introspect runtime contexts and monitor open workload queues on the active loop.
#อยากรู้ว่าใน loop มี task อะไรทำงานอยู่
import asyncio
from time import ctime

async def dynamic_job(number):
    await asyncio.sleep(1.0)

async def main():
    # เช็คชื่อของ task ปัจจุบันที่กำลังทำงานอยู่
    me = asyncio.current_task()
    me.set_name("Main-Coordinator")
    print(f"{ctime()} Active Execution Context Name: {me.get_name()}")
    
    # สร้าง task ใหม่และเพิ่มเข้าไปใน loop
    tasks = [asyncio.create_task(dynamic_job(i), name=f"Job-{i}") for i in range(3)]
    
    # นับจำนวน task ที่กำลังทำงานอยู่ใน loop และแสดงชื่อของแต่ละ task
    all_active = asyncio.all_tasks()
    print(f"{ctime()} Total Active Tasks inside Loop: {len(all_active)}")
    for t in all_active:
        print(f"{ctime()}  -> Active Queue Item: {t.get_name()}")

    await asyncio.sleep(1.1) # สิ้นสุด task ทั้งหมดก่อนที่จะจบ main

asyncio.run(main())