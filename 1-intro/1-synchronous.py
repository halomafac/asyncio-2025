import time
from datetime import datetime

def make_burger(student_id):
    start_timestamp = datetime.now()
    print(f"[{start_timestamp.strftime('%H:%M:%S')}] >>> เริ่มทำเบอร์เกอร์ให้นักเรียนคนที่ {student_id}")
    
    print(f"[{datetime.now().strftime('%H:%M:%S')}] 1. ทอดเบอร์เกอร์...")
    time.sleep(5)

    print(f"[{datetime.now().strftime('%H:%M:%S')}] 2. ทอดไก่...")
    time.sleep(5)

    print(f"[{datetime.now().strftime('%H:%M:%S')}] 3. ใส่ผักและชีส...")
    time.sleep(5)

    print(f"[{datetime.now().strftime('%H:%M:%S')}] 4. ห่อเบอร์เกอร์...")
    time.sleep(5)

    end_timestamp = datetime.now()
    print(f"[{end_timestamp.strftime('%H:%M:%S')}] <<< เสร็จแล้ว! เบอร์เกอร์ของนักเรียนคนที่ {student_id}")
    print(f"-- เวลาที่เริ่ม : {start_timestamp.strftime('%H:%M:%S')}")
    print(f"-- เวลาที่เสร็จ: {end_timestamp.strftime('%H:%M:%S')}")
    print(f"-- ใช้เวลา: {(end_timestamp - start_timestamp).seconds} วินาที\n")

def main():
    all_start = time.time()
    
    for i in range(1, 6):
        make_burger(i)
        
    all_end = time.time()
    print(f"[{datetime.now().strftime('%H:%M:%S')}] รวมเวลาทั้งหมด: {all_end - all_start:.2f} วินาที")

if __name__ == "__main__":
    main()

 