import asyncio
import time

# ---------- Models ----------
class Order:
    def __init__(self, customer: str, items: list[str]):
        self.customer = customer
        self.items = items

# ---------- Producers ----------
async def customer_producer(queue: asyncio.Queue, name: str, items: list[str]):
    order = Order(name, items)
    # ลูกค้าเสร็จจากการซื้อของ และเข้าคิวจ่ายเงิน
    print(f"[{time.ctime()}] [{name}] finished shopping: {items}")
    await queue.put(order)

# ---------- Consumers ----------
async def cashier(name: str, secs_per_item: float, queue: asyncio.Queue):
    try:
        while True:
            order: Order = await queue.get()
            # เริ่มคิดเงิน
            print(f"[{time.ctime()}] [Cashier-{name}] processing {order.customer} with orders {order.items}")
            # คิดเงินทีละชิ้น
            for _ in order.items:
                await asyncio.sleep(secs_per_item)
            # เสร็จงานลูกค้าคนนี้
            print(f"[{time.ctime()}] [Cashier-{name}] finished {order.customer}")
            queue.task_done()
    except asyncio.CancelledError:
        # ปิดเคาน์เตอร์
        print(f"[{time.ctime()}] [Cashier-{name}] closed")
        raise

# ---------- Main ----------
async def main():
    queue = asyncio.Queue()

    # แคชเชียร์ 2 คน: คนละความเร็ว
    c1 = asyncio.create_task(cashier("1", 1.0, queue))  # 1 วินาที/ชิ้น
    c2 = asyncio.create_task(cashier("2", 2.0, queue))  # 2 วินาที/ชิ้น

    # ลูกค้า 3 คน (แต่ละคน = 1 งานบนคิว)
    producers = [
        customer_producer(queue, "Alice",   ["Apple", "Banana", "Milk"]),
        customer_producer(queue, "Bob",     ["Bread", "Cheese"]),
        customer_producer(queue, "Charlie", ["Eggs", "Juice", "Butter"]),
    ]
    await asyncio.gather(*producers)

    # รอให้ทุกออเดอร์ถูกคิดเงินครบ
    await queue.join()

    # ปิดร้าน: ยกเลิกแคชเชียร์ทั้งสอง (ลูปไม่มีวันจบเอง)
    for t in (c1, c2):
        t.cancel()
    for t in (c1, c2):
        try:
            await t
        except asyncio.CancelledError:
            pass

    print(f"[{time.ctime()}] [Main] Supermarket closed!")

if __name__ == "__main__":
    asyncio.run(main())