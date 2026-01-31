from automation.flow_manager import install_flow

THRESHOLD = 5000000

def decide(tx, rx):
    total = tx + rx
    if total > THRESHOLD:
        print("[AGENT IA] Décision : redirection du trafic")
        install_flow(1, 3)
    else:
        print("[AGENT IA] Trafic normal")

# Test
decide(4000000, 2000000)
