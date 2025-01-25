from cube import *
from nolimit import *
from box import *
import tkinter as tk
from tkinter import ttk
import threading #Use Threading for Performance
import subprocess
from credits import *

htop = True


def display_window():
    global htop


    def credss():
        credthread = threading.Thread(target=creds(), daemon=True)
        credthread.start()

    def quitfunction():
        root.destroy()
        exit()

    def button1_action():
        nlthread = threading.Thread(target=run_nl_canvas(), daemon=True)
        nlthread.start()
        root.destroy()  # Should destroy window
        print("Game Launched (box.py)")

    def button2_action():
        nolthread = threading.Thread(target=run_NOL(), deamon=True)
        nolthread.start()
        root.destroy()

    def cube_action():
        cubethread = threading.Thread(target=cuberotate(), deamon=True)
        cubethread.start()

    # Create the main window
    root = tk.Tk()
    root.title("Menu")
    root.geometry("480x420")


    # Apply dark theme colors
    root.configure(bg="#2E2E2E")


    # Create and style Button 1
    style = ttk.Style()
    style.theme_use("clam")
    style.configure(
        "TButton",
        background="#444444",
        foreground="white",
        font=("Arial", 12),
        borderwidth=1,
        focuscolor="#444444",
    )

    button1 = ttk.Button(root, text="Run Game Normally!", command=button1_action)
    button1.pack(pady=20)

    # Create and style Button 2
    button2 = ttk.Button(root, text="Run Endless!", command=button2_action)
    button2.pack(pady=20)

    cubebtn = ttk.Button(root, text="TkInter Test", command=cube_action)
    cubebtn.pack(pady=20)

    # Add Quit button
    quitbutton = ttk.Button(root, text="Quit", command=quitfunction)
    quitbutton.pack(pady=20)

    creadbtn = ttk.Button(root, text="Credits", command=credss)
    creadbtn.pack(pady=20)

    # Run the main loop
    root.mainloop()


display_window()
