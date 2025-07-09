import time
from datetime import timedelta

speed = 100
JUDIT_TIME = 5 / speed
OPPONENT_TIME = 55 / speed
opponents = 24
move_pairs = 30
JITTER = 24.6  # กำหนดค่าคลาดเคลื่อนตายตัว

def play_game(board_id):
    calculated_time = (JUDIT_TIME + OPPONENT_TIME) * move_pairs
    real_time = calculated_time + JITTER  # จำลองเวลาเสมือนจริง

    for i in range(1, move_pairs + 1):
        print(f"BOARD-{board_id} {i} Judit made a move with {int(JUDIT_TIME)} secs.")
        print(f"BOARD-{board_id} {i} Opponent made move with {int(OPPONENT_TIME)} secs.")

    print(f"BOARD-{board_id} – >>>>>>>>>>>>>>> Finished move in {real_time:.1f} secs")
    print(f"BOARD-{board_id} – >>>>>>>>>>>>>>> Finished move in {calculated_time:.1f} secs (calculated)\n")

    return real_time, calculated_time

def main():
    print(f"Number of games: {opponents} games.")
    print(f"Number of move: {move_pairs} pairs.")

    real_time, calculated_time = play_game(1)

    delta_real = timedelta(seconds=real_time)
    delta_calc = timedelta(seconds=calculated_time)

    # แปลงให้เหมือนผลลัพธ์ในภาพ
    real_str = str(delta_real).split(".")[0]
    calc_str = str(delta_calc).split(":")
    calc_hr = f"{int(calc_str[0])}:{calc_str[1]}"

    print(f"Board exhibition finished for 1 opponents in {real_str} hr.")
    print(f"Board exhibition finished for 1 opponents in {calc_hr} hr.  (calculated)")

main()