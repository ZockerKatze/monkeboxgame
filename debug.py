"""
This debugging tool works as should but only for certain tasks that it can find

If you want to use this, you need to change SYSTEMD from the pname!


"""


import psutil
import time
import os

stop_thread = False  # Global flag

def readPID():
    global stop_thread
    process_name = "systemd"

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

                    print(f"{"╠"}{"═"*43}ProcMan{"═"*43}{"╣"}")

                    print(f"ProcessName →→→ {process_name}")

                    print(f"{"╠"}{"═"*100}{"╣"}")

                    print(f"PID →→→ {pid}")

                    print(f"{"╠"}{"═"*100}{"╣"}")

                    print(f"CPU Use →→→ {cpu_usage}%")

                    print(f"{"╠"}{"═"*100}{"╣"}")

                    print(f"Memory Use →→→ {memory_usage:.2f} MB")

                    print(f"{"╠"}{"═"*100}{"╣"}")

            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass

        if not found:
            print(f"Proc {process_name} not found!")

        time.sleep(0.5)

readPID()
