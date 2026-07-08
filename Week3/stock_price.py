# นักเรียนต้องเลือกใช้ asyncio.wait() พร้อมออปชัน return_when=asyncio.FIRST_COMPLETED เท่านั้น (หากใครใช้ gather หรือ wait_for จะไม่ตรงสเปกเงื่อนไขการแข่งส่งข้อมูล)
import asyncio
 
 
async def fetch_stock_price(server_name: str, delay: float) -> str:
    """Coroutine จำลองการดึงราคาหุ้นจากเซิร์ฟเวอร์ 1 สาขา"""
    await asyncio.sleep(delay)
    return f"[{server_name}] Price: 150 USD"
 
 
async def main() -> None:
    servers = {
        "Alpha": 3.0,
        "Beta": 0.8,
        "Gamma": 1.5,
    }
 
    # แตก Task ทั้ง 3 สาขาให้ทำงานพร้อมกันใน Event Loop
    tasks = [
        asyncio.create_task(fetch_stock_price(name, delay), name=name)
        for name, delay in servers.items()
    ]
 
    # ใช้ wait() แทน gather() เพราะต้องการ "หลุดออกจากการรอ" ทันที
    # เมื่อมีตัวใดตัวหนึ่งเสร็จก่อน (gather ต้องรอครบทุกตัวเสมอ ทำแบบนี้ไม่ได้)
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
 
    winner_task = done.pop()
    print(f"ผู้ชนะการแข่งขัน (ไวที่สุด): {winner_task.result()}  <- Task '{winner_task.get_name()}'")
 
    # [Anti-Memory Leak] วนลูปยกเลิกงานที่เหลือค้างอยู่ (pending) ให้หมดสิ้น
    for task in pending:
        print(f"ยกเลิกงานของ Task '{task.get_name()}' ที่ยังทำงานค้างอยู่...")
        task.cancel()
 
    # รอให้การยกเลิกเสร็จสมบูรณ์จริง ๆ ก่อนจบโปรแกรม (กัน task ค้าง/warning)
    if pending:
        await asyncio.gather(*pending, return_exceptions=True)
 
    print("เคลียร์ระบบเรียบร้อย ไม่มีงานค้างในเครือข่ายแล้ว")
 
 
if __name__ == "__main__":
    asyncio.run(main())