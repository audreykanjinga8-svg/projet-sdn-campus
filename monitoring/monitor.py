import time
from datetime import datetime
import os  # pour le son beep Linux

# Seuil de congestion
THRESHOLD = 5_000_000  # 5 MB

def get_fake_stats():
    
    import random
    tx = random.randint(1_000_000, 8_000_000)
    rx = random.randint(1_000_000, 8_000_000)
    return tx, rx

print("🔹 Monitoring réseau démarré. Appuyez sur CTRL+C pour arrêter.")

try:
    while True:
        tx, rx = get_fake_stats()
        total = tx + rx
        now = datetime.now().strftime("%H:%M:%S")

        # Affichage des statistiques
        print(f"[{now}] [MONITOR] TX={tx} RX={rx} TOTAL={total}")

        # Détection d'anomalie
        if total > THRESHOLD:
             # Alerte visible + son
            print(f"\033[91m[{now}] [ALERTE] Congestion détectée 🚨\033[0m")
            print("\a")  # bip terminal

        time.sleep(5)

except KeyboardInterrupt:
    print("\n🛑 Monitoring arrêté par l'utilisateur.")
