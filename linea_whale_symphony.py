import requests, time

def linea_symphony():
    print("Linea — Whale Symphony Conductor (>$1M moves only)")
    seen = set()
    while True:
        r = requests.get("https://api.lineascan.build/api?module=account&action=txlist&address=0x0000000000000000000000000000000000000000&sort=desc")
        for tx in r.json()["result"][:35]:
            h = tx["hash"]
            if h in seen: continue
            seen.add(h)
            value = int(tx["value"]) / 1e18
            if value > 1000:  # >1000 ETH equivalent
                print(f"♪♫ WHALE SYMPHONY INCOMING ♫♪\n"
                      f"♬ {value:,.2f} ETH just moved on Linea\n"
                      f"♬ From: {tx['from'][:12]}...\n"
                      f"♬ To:   {tx['to'][:12]}...\n"
                      f"♬ https://lineascan.build/tx/{h}\n"
                      f"♬ The orchestra is warming up — listen carefully\n"
                      f"{'🎻🎺🎷'*12}\n")
        time.sleep(2.1)

if __name__ == "__main__":
    linea_symphony()
