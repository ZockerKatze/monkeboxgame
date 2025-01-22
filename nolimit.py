import tkinter as tk
import random

def run_NOL():
    def create_random_box():
        nonlocal box_size
        canvas.delete("box")

        # Generate random coordinates for the box
        x1 = random.randint(50, screen_width - 50 - box_size)
        y1 = random.randint(50, screen_height - 50 - box_size)
        x2 = x1 + box_size
        y2 = y1 + box_size

        # Create the box
        box = canvas.create_rectangle(x1, y1, x2, y2, fill="white", tags="box")
        canvas.tag_bind("box", "<Button-1>", on_box_click)

    def callpause(event=None):
        # Create a semi-transparent overlay
        pauseoverlay = tk.Frame(canvas, width=screen_width, height=screen_height, bg="black")
        pauseoverlay.place(x=0, y=0)

        # Add a label to the overlay
        pauselabel = tk.Label(pauseoverlay, text="PAUSED", font=("Helvetica", 40), fg="white", bg="black")
        pauselabel.pack(pady=40)

        # Define the exit and continue buttons
        def exitgame():
            root.quit()
            exit()

        def continuegame():
            pauseoverlay.place_forget()

        exitbutton = tk.Button(pauseoverlay, text="Exit", command=exitgame, font=("Helvetica", 40))
        exitbutton.pack(pady=100)

        continuebutton = tk.Button(pauseoverlay, text="Continue", command=continuegame, font=("Helvetica", 40))
        continuebutton.pack(pady=100)

    def on_box_click(event):
        nonlocal score
        score += 1
        update_score()
        create_random_box()

    def update_score():
        score_label.config(text=f"Score: {score}")

    def exit_fullscreen(event):
        root.attributes("-fullscreen", False)

    def exit_window(event=None):
        root.quit()

    # Initialize main window
    root = tk.Tk()
    root.title("MONKEEEEEEEEEEEE SIM")
    root.attributes("-fullscreen", True)

    # Screen dimensions
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Variables
    initial_box_size = 200
    box_size = initial_box_size
    size_reduction_step = 40  # Amount to reduce the size per 100 points
    score = 0

    # Create canvas
    canvas = tk.Canvas(root, width=screen_width, height=screen_height, bg="black")
    canvas.pack(fill="both", expand=True)

    # Create score label
    score_label = tk.Label(root, text=f"Score: {score}", font=("Arial", 24), bg="black", fg="white")
    score_label.place(x=screen_width - 400, y=10)

    # Bind events
    root.bind("<Escape>", callpause)
    root.bind("<Control-q>", exit_window)

    create_random_box()
    root.mainloop()

# To run the game, call run_nl_canvas()
if __name__ == "__main__":
    run_NOL()

