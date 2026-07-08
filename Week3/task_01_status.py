# Objective: Learn how to query the lifecycle status of a task object. 
import asyncio
from time import ctime

async def short_job():
    await asyncio.sleep(1)
    return "Success"

async def main():
    task = asyncio.create_task(short_job())
    
    # เช็คสถานะของ task ก่อนที่จะ await
    print(f"{ctime()} Is task done? {task.done()}")          # คาดหวังว่า task ยังไม่เสร็จ
    print(f"{ctime()} Is task canceled? {task.cancelled()}")  # คาดหวังว่า task ยังไม่ถูกยกเลิก
    
    await task # รอคจนกว่า task จะเสร็จสิ้น
    
    # อยากรู้ว่า task เสร็จแล้วหรือยังหลังจาก await
    print(f"{ctime()} Is task done now? {task.done()}")      # คาดหวังว่า task เสร็จแล้ว
    print(f"{ctime()} Is task canceled now? {task.cancelled()}") # คาดหวังว่า task ยังไม่ถูกยกเลิก

asyncio.run(main())