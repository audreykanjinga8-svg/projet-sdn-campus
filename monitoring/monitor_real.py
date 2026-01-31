import time
import random
from agent.ai_agent import decide

THRESHOLD = 5000000

def get_stats():
    tx = random.randint(1_000_000, 9_000_000)
    rx = random.randint(1_000_000, 9_000_000)
    return tx, rx

while True:
    tx, rx = get_stats()
    total = tx + rx

    print(f"[MONITOR] TX={tx} RX={rx} TOTAL={total}")

    decide(tx, rx)

    time.sleep(5)

