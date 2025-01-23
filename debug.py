import os
import psutil
import time

## <!NOTE! -- Change PID name to actuall name of Tkinter Window for the process ENDL -- >

def readPID():
    pname = "asdf.py"

    while True:
        os.system("clear")
        found = False

        for process in psutil.process_iter(["pid","name","cpu_process","memory_info"]):
            try:
                if process.info["name"] == process_name:
                    found = True
                    pid = process.info["pid"]
                    cpu_usage = process.info["cpu_precent"]
                    memory_usage = process.info["memory_info"].rss / (1024*1024)

                    print(f"ProcessName: {process_name}")
                    print(f"PID: {pid}")
                    print(f"CPU Use: {cpu_usage}%")
                    print(f"Memory Use: {memory_usage:.2f} MB")

            except (psutil.NoSuchProcess, psutil.AcessDenied, psutil.ZombieProcess):
                pass

        if not found:
            print(f"Proc {process_name} not found!")

        time.sleep(2)



readPID()
