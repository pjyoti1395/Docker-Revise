import time
from datetime import datetime

while True:
    with open("/app/data/log.txt", "a") as f:
        f.write(f"{datetime.now()} - Hello from container!\n")
    time.sleep(5)
