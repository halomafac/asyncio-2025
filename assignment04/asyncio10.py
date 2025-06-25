# call back task
import asyncio

async def simple_task():
    await asyncio.sleep(1)
    return "งานเสร็จสิ้น"

def on_done(task):
    print("Callblack: ", task.result())

async def main():
    task = asyncio.create_task(simple_task())
    task.add_done_callback(on_done)
    await task

asyncio.run(main())