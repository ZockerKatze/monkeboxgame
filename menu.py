from nolimit import *
from box import *
import tkinter as tk
from tkinter import ttk
from debug import readPID
import threading


def display_window():
    def quitfunction():
        root.destroy()
        exit()

    def button1_action():
        run_nl_canvas()
        root.destroy()  # Should destroy window
        print("Game Launched (box.py)")

    def button2_action():
        run_NOL()
        root.destroy()

    #def debug_action():
                            # make a new thread here because the debug was cockblocking the tkinter app

    #    debug_thread = threading.Thread(target=readPID, daemon=True)
    #    debug_thread.start()



    # Create the main window
    root = tk.Tk()
    root.title("Menu")
    root.geometry("480x320")


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

    # Add Debug button
    debugbtn = ttk.Button(root, text="Debug", command=debug_action)
    debugbtn.pack(pady=20)

    # Add Quit button
    quitbutton = ttk.Button(root, text="Quit", command=quitfunction)
    quitbutton.pack(pady=20)

    # Run the main loop
    root.mainloop()


display_window()
