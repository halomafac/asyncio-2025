import time
from multiprocessing import Process
from datetime import datetime

def make_burger(student_id):
    start_time = datetime.now()
    print(f"[{start_time.strftime('%H:%M:%S')}] >>> เริ่มทำเบอร์เกอร์ให้นักเรียนคนที่ {student_id}")
    
    print(f"[{datetime.now().strftime('%H:%M:%S')}] 1. ทอดเบอร์เกอร์... ({student_id})")
    time.sleep(5)

    print(f"[{datetime.now().strftime('%H:%M:%S')}] 2. ทอดไก่... ({student_id})")
    time.sleep(5)

    print(f"[{datetime.now().strftime('%H:%M:%S')}] 3. ใส่ผักและชีส... ({student_id})")
    time.sleep(5)

    print(f"[{datetime.now().strftime('%H:%M:%S')}] 4. ห่อเบอร์เกอร์... ({student_id})")
    time.sleep(5)

    end_time = datetime.now()
    print(f"[{end_time.strftime('%H:%M:%S')}] <<< เสร็จแล้ว! เบอร์เกอร์ของนักเรียนคนที่ {student_id}")
    print(f"-- เวลาที่เริ่ม : {start_time.strftime('%H:%M:%S')} | นักเรียน {student_id}")
    print(f"-- เวลาที่เสร็จ: {end_time.strftime('%H:%M:%S')} | นักเรียน {student_id}")
    print(f"-- ใช้เวลา: {(end_time - start_time).seconds} วินาที | นักเรียน {student_id}\n")

def main():
    start = time.time()
    
    processes = []
    for i in range(1, 100):
        p = Process(target=make_burger, args=(i,))
        processes.append(p)
        p.start()
    
    for p in processes:
        p.join()
    
    end = time.time()
    print(f"[{datetime.now().strftime('%H:%M:%S')}] รวมเวลาทั้งหมด: {end - start:.2f} วินาที")

if __name__ == "__main__":
    main()
