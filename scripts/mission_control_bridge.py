#!/usr/bin/env python3
import requests
import time

MISSION_CONTROL_URL = "http://127.0.0.1:4000/api/heartbeat"

def report_status(task="Video Production Ready"):
    payload = {
        "agent": "VideoExpress Studio Agent",
        "task": task,
        "status": "ONLINE",
        "timestamp": time.time()
    }
    try:
        res = requests.post(MISSION_CONTROL_URL, json=payload, timeout=2)
        print(f"✓ Mission Control notified: HTTP {res.status_code}")
    except Exception as e:
        print(f"⚠ Mission Control ping failed: {e}")

if __name__ == "__main__":
    report_status()
