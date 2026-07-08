# Objective: Implement complex processing workflows based on task fulfillment conditions.
import asyncio
from time import ctime

async def network_probe(server_name, delay):
    await asyncio.sleep(delay)
    return f"Ping successful: {server_name}"

async def main():
    # สร้าง task ใหม่และเพิ่มเข้าไปใน loop
    tasks = {
        asyncio.create_task(network_probe("Primary-Server", 2.0)),
        asyncio.create_task(network_probe("Backup-Server-1", 0.5)),
        asyncio.create_task(network_probe("Backup-Server-2", 1.0))
    }
    
    # เอา task ที่เสร็จสิ้นและ task ที่ยังคงอยู่ (FIRST_COMPLETED เป็นตัวกำหนดเงื่อนไขการรอคอย)
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED) #(All_COMPLETED, FIRST_EXCEPTION))
    
    print(f"{ctime()} Count of Tasks Done: {len(done)}")       # 
    print(f"{ctime()} Count of Tasks Pending: {len(pending)}") # 
    
    for finished_task in done:
        print(f"{ctime()} Fastest Task Result: {finished_task.result()}")
        
    # ยกเลิก task ที่ยังคงอยู่
    for ongoing_task in pending:
        ongoing_task.cancel()
    #เราจะได้มา 1 task ที่เสร็จสิ้นและ 2 task ที่ยังคงอยู่ (ซึ่งเราจะยกเลิกมัน) เพราะเรากำหนดเงื่อนไขการรอคอยเป็น FIRST_COMPLETED
asyncio.run(main())