# example of using an asyncio queue
from random import random
import asyncio
import time

# producer: สร้างงานและใส่คิว
async def producer(queue: asyncio.Queue):
    print(f"{time.ctime()} Producer: Running")
    for i in range(10):
        # สร้างค่าและหน่วงเวลาให้เหมือนทำงานจริง
        value = i
        sleep_t = random()
        print(f"{time.ctime()} -> Producer {value} sleep {sleep_t:.3f}")
        await asyncio.sleep(sleep_t)
        await queue.put(value)
        print(f"{time.ctime()} -> Producer put {value}")
    # ส่งสัญญาณจบงาน
    await queue.put(None)
    print(f"{time.ctime()} Producer: Done")

# consumer: ดึงงานแบบ block (รอคิว)
async def consumer(queue: asyncio.Queue):
    print(f"{time.ctime()} Consumer: Running")
    while True:
        item = await queue.get()  # block จนกว่าจะมีของ
        if item is None:
            break
        print(f"{time.ctime()}\t> Consumer got {item}")
        # หน่วงเหมือนประมวลผล
        await asyncio.sleep(0.2)
    print(f"{time.ctime()} Consumer: Done")

# main
async def main():
    queue = asyncio.Queue()
    await asyncio.gather(producer(queue), consumer(queue))

if __name__ == "__main__":
    asyncio.run(main())