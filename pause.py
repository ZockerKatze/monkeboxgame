
def show_pause_screen(canvas):
    # Create a transparent overlay frame
    pause_overlay = tk.Frame(canvas, width=canvas.winfo_width(), height=canvas.winfo_height(), bg='gray', opacity=0.5)
    pause_overlay.place(x=0, y=0)

    # Display pause text
    pause_label = tk.Label(pause_overlay, text="PAUSED", font=("Helvetica", 24), fg="white", bg="black")
    pause_label.pack(pady=20)

    # Define exit function
    def exit_game():
        canvas.master.quit()

    # Define continue function
    def continue_game():
        pause_overlay.place_forget()  # Hide the pause screen

    # Add buttons for options
    exit_button = tk.Button(pause_overlay, text="Exit", command=exit_game, font=("Helvetica", 14))
    exit_button.pack(pady=10)
    
    continue_button = tk.Button(pause_overlay, text="Continue", command=continue_game, font=("Helvetica", 14))
    continue_button.pack(pady=10)
