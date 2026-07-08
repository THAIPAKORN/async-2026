# Objective: Group multiple operations to run concurrently and return an ordered list of outputs.
#รวมหลายๆ task ให้ทำงานพร้อมกันและส่งผลลัพธ์ออกมาเป็น list
import asyncio
from time import time, ctime

async def fetch_db_record(table_name, latency):
    await asyncio.sleep(latency)
    return f"RowData_{table_name}"

async def main():
    start = time()
    
    # รัน task ทั้งหมดพร้อมกันและรอให้เสร็จสิ้น
    results = await asyncio.gather(
        fetch_db_record("Users", 1.0),
        fetch_db_record("Products", 0.5),
        fetch_db_record("Invoices", 1.0)
    )
    
    print(f"{ctime()} Aggregated Output Results List: {results}")
    print(f"{ctime()} Execution Completed in: {time() - start:.2f} seconds") #คาดหวังว่าใช้เวลาไม่เกิน 1.0 วินาทีเพราะ task ทั้งหมดทำงานพร้อมกัน
    #รอจนกว่า task ทั้งหมดจะเสร็จสิ้นและส่งผลลัพธ์ออกมาเป็น list ต่อให้ products จะเสร็จก่อน users และ invoices ก็ตาม
asyncio.run(main())