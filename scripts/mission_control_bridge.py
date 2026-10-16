import requests
import sys
import json
import time

MISSION_CONTROL_URL = "http://127.0.0.1:4000/api/tasks/complete"

def notify_mission_control(video_title, duration, export_url):
    payload = {
        "task_name": f"Video Production: {video_title}",
        "agent": "Hermes VideoExpress Agent",
        "duration": duration,
        "export_url": export_url,
        "status": "SHIPPED",
        "timestamp": time.time()
    }
    try:
        res = requests.post(MISSION_CONTROL_URL, json=payload, timeout=5)
        print(f"✓ Dispatched to Imboni Mission Control: HTTP {res.status_code}")
    except Exception as e:
        print(f"⚠ Mission Control dispatch offline: {e}")

if __name__ == "__main__":
    notify_mission_control("BlockMaster Factory Demo", "60s", "https://storage.imbonigroup.com/exports/demo.mp4")
