import time

THRESHOLD = 5000000  # 5 MB

def get_fake_stats():
    """
    Simulation de stats réseau (pour commencer).
    Plus tard, on branchera les vraies stats OpenFlow.
    """
    import random
    tx = random.randint(1_000_000, 8_000_000)
    rx = random.randint(1_000_000, 8_000_000)
    return tx, rx

while True:
    tx, rx = get_fake_stats()
    total = tx + rx

    print(f"[MONITOR] TX={tx} RX={rx} TOTAL={total}")

    if total > THRESHOLD:
        print("[ALERTE] Congestion détectée 🚨")

    time.sleep(5)
