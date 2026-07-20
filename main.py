import time
from datetime import datetime

PAIRS = [
    "EURUSD",
    "GBPUSD",
    "USDJPY",
    "XAUUSD"
]

def scan():
    print("=" * 50)
    print("AI Trader X")
    print("Time:", datetime.now())
    print("=" * 50)

    for pair in PAIRS:
        print(f"Scanning {pair}...")

    print("Scan complete.\n")

while True:
    scan()
    time.sleep(60)
