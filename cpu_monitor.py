import psutil
import time

threshold = 30

# ANSI code for red text

RED = "\033[91m"
RESET = "\033[0m"

print("Monitoring CPU usage...")

psutil.cpu_percent(interval=None)

try:
    while True:
        cpu_usage = psutil.cpu_percent(interval=1)
        print(f"CPU usage: {cpu_usage}%")

        if cpu_usage > threshold:
            print(f"{RED}Alert! CPU usage exceeds threshold ({threshold}%): {cpu_usage}%{RESET}")

        time.sleep(1)

except KeyboardInterrupt:
    print("Monitoring stopped by user.")