import time
import asyncio
import httpx

student_id = "6610301002"   # 🔹ใส่รหัสนักศึกษาของคุณเอง
ROCKET_URL = f"http://172.16.2.117:8088/fire/{student_id}"

async def fire_rocket(name: str, t0: float):
    """ยิง rocket 1 ลูก แล้วคืนค่าข้อมูลเวลาต่างๆ"""
    start_time = time.perf_counter() - t0  # เวลาเริ่มสัมพัทธ์

    async with httpx.AsyncClient() as client:
        resp = await client.get(ROCKET_URL)
        resp.raise_for_status()
        data = resp.json()

    # สมมติ response เป็น {"time_to_target": 1.73}
    time_to_target = float(data["time_to_target"])

    end_time = time.perf_counter() - t0     # เวลาเมื่อ request เสร็จ
    return {
        "name": name,
        "start_time": start_time,
        "time_to_target": time_to_target,
        "end_time": end_time
    }

async def main():
    t0 = time.perf_counter()     # เวลาเริ่มของชุด rockets
    print("Rocket prepare to launch ...")

    # 🔹 สร้าง task ยิง rocket 3 ลูกพร้อมกัน
    tasks = [
        asyncio.create_task(fire_rocket("Rocket-1", t0)),
        asyncio.create_task(fire_rocket("Rocket-2", t0)),
        asyncio.create_task(fire_rocket("Rocket-3", t0))
    ]

    # 🔹 รอให้ทุก task เสร็จ
    results = await asyncio.gather(*tasks)

    # 🔹 เรียงตามเวลาถึงจุดหมาย (end_time หรือ time_to_target ก็ได้คล้ายกัน)
    results.sort(key=lambda r: r["end_time"])

    print("Rockets fired:")
    for r in results:
        print(f"{r['name']} | start_time: {r['start_time']:.2f} sec "
              f"| time_to_target: {r['time_to_target']:.2f} sec "
              f"| end_time: {r['end_time']:.2f} sec")

    # 🔹 เวลารวมทั้งหมด (ลูกที่มาถึงช้าที่สุด)
    t_total = max(r["end_time"] for r in results)
    print(f"\nTotal time for all rockets: {t_total:.2f} sec")


if __name__ == "__main__":
    asyncio.run(main())

