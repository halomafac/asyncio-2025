# Check if a Task is Done
import asyncio

async def simple_task():
    await asyncio.sleep
    return "เสร็จเเล้ว!"

async def main():
    task = asyncio.create_task(simple_task())
    print("ก่อน await:", task.done()) #ยังไม่เสร็จ
    await task
    print("หลัง await", task.done) #เสร็จเเล้ว

asyncio.run(main())
