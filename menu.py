from nolimit import *
from box import *
import tkinter as tk
from tkinter import ttk
from debug import RMon, readPID
import os

def display_window():
    # Function to be called when Button 1 is clicked
    def quitfunction():
        root.destroy()
        exit()

    def debug():
        debug.readPID()
        print("debug true")


    def button1_action():
        run_nl_canvas()
        root.destroy() ## should destroy window
        print("GameLaunched (box.py) ")
    # Function to be called when Button 2 is clicked
    def button2_action():
        run_NOL()
        root.destroy()

    # Create the main window
    root = tk.Tk()
    root.title("Menu")
    root.geometry("480x320")

    # Apply dark theme colors
    root.configure(bg="#2E2E2E")

    # Create and style Button 1
    style = ttk.Style()
    style.theme_use("clam")
    style.configure("TButton",
                    background="#444444",
                    foreground="white",
                    font=("Arial", 12),
                    borderwidth=1,
                    focuscolor="#444444")

    button1 = ttk.Button(root, text="Run Game Normally!", command=button1_action)
    button1.pack(pady=20)

    # Create and style Button 2
    button2 = ttk.Button(root, text="Run Endless!", command=button2_action)
    button2.pack(pady=20)

    # make button for debugmode

    debugbtn = ttk.Button(root, text="Debug", command=debug)
    debugbtn.pack(pady=20)

    quitbutton = ttk.Button(root, text="Quit",command=quitfunction)
    quitbutton.pack(pady=20)

    # Run the main loop
    root.mainloop()


display_window()
