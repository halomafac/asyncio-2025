# Hint:
# โค้ดนี้จะพิมพ์ "All tasks scheduled" แล้วจบ ทันที
# เพราะแม้จะ create_task() แต่ถ้าไม่ await มัน → main() จบก่อน → loop ถูกปิด → task ถูก cancel
# ผลลัพธ์คือไม่มี task ไหนทำงานเสร็จจริง

# Result:
# Task-0 started
# Task-1 started
# Task-2 started
# Task-0 finished
# Task-1 finished
# Task-2 finished
# Results: [1, 2, 3]

import asyncio

async def work(n):
    print(f"Start {n}")
    await asyncio.sleep(1)
    print(f"Done {n}")
    return n

async def main():
    results1 = []
    for i in range(3):
        results1.append(asyncio.create_task(work(i)))
    result1 = []
    for r in results1:
        result1.append(await r)
    print("Results1:", result1)

    results2 = []
    for i in range(3, 6):
        results2.append(asyncio.create_task(work(i)))
    result2 = []
    for r in results2:
        result2.append(await r)
    print("Results2:", result2)

asyncio.run(main())
