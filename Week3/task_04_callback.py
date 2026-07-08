# Objective: Attach a plain synchronous function that automatically triggers the moment a task finishes.
import asyncio
from time import ctime

def alert_manager(finished_task):
    # บอกว่า task เสร็จแล้วและดึงผลลัพธ์ออกมา
    print(f"{ctime()} Callback Triggered! Task output fetched: {finished_task.result()}")

async def download_file():
    #ไปโหลดไฟล์จาก server
    print(f"{ctime()} Downloading packet...")
    await asyncio.sleep(1.0)
    return "Data_Payload.zip"

async def main():
    task = asyncio.create_task(download_file())
    # พอรัน task เสร็จแล้วก็จะเรียก callback function ที่เรากำหนดไว้
    task.add_done_callback(alert_manager)
    
    await task # รอคจนกว่า task จะเสร็จสิ้น

asyncio.run(main())