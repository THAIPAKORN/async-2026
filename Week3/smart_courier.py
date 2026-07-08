# Delivery System): นักศึกษาต้องเขียน try...except CancelledError ได้ถูกต้อง 
# และใช้ .get_name(), .cancel(), และ .cancelled() ได้
import asyncio
 
 
async def delivery_task(package_id: str, duration: float) -> str:
    """Coroutine จำลองการส่งพัสดุ 1 ชิ้น"""
    print(f"[{package_id}] เริ่มส่งพัสดุ... (คาดว่าจะใช้เวลา {duration} วินาที)")
    try:
        await asyncio.sleep(duration)
    except asyncio.CancelledError:
        # ข้อ 5: ดักจับ CancelledError ในตัวคูรูทีนส่งของโดยตรง
        print("Delivery Canceled! Returning package to warehouse.")
        # สำคัญ: ต้อง re-raise ต่อ ไม่เช่นนั้น Task จะไม่ถูกมาร์กว่า "cancelled" จริง ๆ
        raise
 
    print(f"[{package_id}] ส่งของสำเร็จแล้ว!")
    return f"Package {package_id} Delivered!"
 
 
async def main() -> None:
    # ข้อ 2: สร้าง Task จาก delivery_task พร้อมตั้งชื่อ Task
    task = asyncio.create_task(
        delivery_task(package_id="P001", duration=5.0),
        name="Express-Courier",
    )
 
    # ข้อ 3: จำลองเวลาผ่านไป 2 วินาทีระหว่างพัสดุกำลังเดินทาง
    await asyncio.sleep(2)
    print(f"[ตรวจสอบ] Task '{task.get_name()}' เสร็จหรือยัง? -> done() = {task.done()}")
 
    # ข้อ 4: ถ้าผ่านไป 2 วินาทีแล้วยังไม่เสร็จ ให้ยกเลิกงานทันที
    if not task.done():
        print(f"[แจ้งเตือน] '{task.get_name()}' ใช้เวลานานเกินไป กำลังสั่งยกเลิก...")
        task.cancel()
 
    # รอผลลัพธ์สุดท้ายของ Task (ไม่ว่าจะเสร็จปกติหรือถูกยกเลิก)
    try:
        result = await task
        print(f"[ผลลัพธ์] {result}")
    except asyncio.CancelledError:
        # CancelledError จะลอยขึ้นมาถึงจุดนี้อีกครั้ง เพราะเรา re-raise ไว้ใน delivery_task
        print(f"[ยืนยันสถานะ] task.cancelled() = {task.cancelled()}")
 
 
if __name__ == "__main__":
    asyncio.run(main())
 