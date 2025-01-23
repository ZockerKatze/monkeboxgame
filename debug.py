import psutil
import time
import os

stop_thread = False  # Global flag

def readPID():
    global stop_thread
    process_name = "python3 menu.py"

    while not stop_thread:
        os.system("clear")
        found = False

        for process in psutil.process_iter(["pid", "name", "cpu_times", "memory_info"]):
            try:
                if process.info["name"] == process_name:
                    found = True
                    pid = process.info["pid"]
                    cpu_usage = process.info["cpu_times"]
                    memory_usage = process.info["memory_info"].rss / (1024 * 1024)

                    print(f"ProcessName: {process_name}")
                    print(f"PID: {pid}")
                    print(f"CPU Use: {cpu_usage}%")
                    print(f"Memory Use: {memory_usage:.2f} MB")

            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass

        if not found:
            print(f"Proc {process_name} not found!")

        time.sleep(2)
