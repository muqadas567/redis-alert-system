import os
import time
import redis

# Docker Compose mein service ka naam hi host ban jata hai
REDIS_HOST = os.getenv('REDIS_HOST', 'localhost')
REDIS_PORT = int(os.getenv('REDIS_PORT', 6379))

print(f"Connecting to Redis at {REDIS_HOST}:{REDIS_PORT}...")

# Redis Connection Setup
try:
    r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)
    # Check connection
    if r.ping():
        print("Successfully connected to Redis!")
except Exception as e:
    print(f"Redis Connection Failed: {e}")
    exit(1)

# 1. Queue mein ek Fake Alert push karte hain
alert_message = "CRITICAL: Selenium Script Failed on Node 1"
print(f"Sending to Queue: {alert_message}")
r.rpush('alert_queue', alert_message)

time.sleep(2) # Thoda gap dene ke liye

# 2. Queue se alert ko fetch (pop) karte hain process karne ke liye
received_alert = r.lpop('alert_queue')
if received_alert:
    print(f" Processing Alert from Queue: {received_alert}")
    print("Notification sent successfully to Admin!")
else:
    print("Queue is empty.")