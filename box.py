import tkinter as tk
import random

def create_random_box():
    global box_size
    canvas.delete("box")

    # Adjust box size based on score
    if score >= 1000:
        box_size = max(50, initial_box_size - (score // 100 * size_reduction_step))

    # Generate random coordinates for the box
    x1 = random.randint(50, screen_width - 50 - box_size)
    y1 = random.randint(50, screen_height - 50 - box_size)
    x2 = x1 + box_size
    y2 = y1 + box_size

    # Create the box
    box = canvas.create_rectangle(x1, y1, x2, y2, fill="white", tags="box")
    canvas.tag_bind("box", "<Button-1>", on_box_click)

def on_box_click(event):
    global score
    score += 1
    update_score()
    create_random_box()

def update_score():
    score_label.config(text=f"Score: {score}")

def exit_fullscreen(event):
    root.attributes("-fullscreen", False)

def exit_window(event=None):
    root.destroy

## init main window

root = tk.Tk()
root.title("MONKEEEEEEEEEEEE SIM")
root.attributes("-fullscreen", True)

## screen width && height

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

## variables

initial_box_size = 200
box_size = initial_box_size
size_reduction_step = 10  # Amount to reduce the size per 100 points
score = 0

# Create canvas
canvas = tk.Canvas(root, width=screen_width, height=screen_height, bg="black")
canvas.pack(fill="both", expand=True)

# Create score label
score_label = tk.Label(root, text=f"Score: {score}", font=("Arial", 24), bg="black", fg="white")
score_label.place(x=screen_width - 400, y=10)

root.bind("<Escape>", exit_fullscreen)
root.bind("<Control-q>", exit_window)

create_random_box()
root.mainloop()

