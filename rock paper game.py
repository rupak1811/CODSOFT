import tkinter as tk
from tkinter import ttk
import random

def play_game(user_choice):
    choices = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(choices)
    user_choice_label.config(text=f"Your Choice: {user_choice}")
    computer_choice_label.config(text=f"Computer's Choice: {computer_choice}")
    
    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
         (user_choice == 'Paper' and computer_choice == 'Rock') or \
         (user_choice == 'Scissors' and computer_choice == 'Paper'):
        result = "You Win!"
    else:
        result = "You Lose!"
        
    result_label.config(text=result)

# Initialize the main window
root = tk.Tk()
root.title("Rock-Paper-Scissors Game")
root.geometry("400x300")

# Optional: Using ttk for better styling
style = ttk.Style(root)
style.configure('TButton', font=('Helvetica', 12))
style.configure('TLabel', font=('Helvetica', 12))

# Title label
title_label = ttk.Label(root, text="Rock-Paper-Scissors", font=('Helvetica', 16))
title_label.pack(pady=10)

# Label to display choices
user_choice_label = ttk.Label(root, text="Your Choice: ", font=('Helvetica', 14))
user_choice_label.pack(pady=5)

computer_choice_label = ttk.Label(root, text="Computer's Choice: ", font=('Helvetica', 14))
computer_choice_label.pack(pady=5)

# Label to display result
result_label = ttk.Label(root, text="", font=('Helvetica', 14))
result_label.pack(pady=20)

# Frame to hold buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

# Buttons for Rock, Paper, Scissors
rock_button = ttk.Button(button_frame, text="Rock", command=lambda: play_game('Rock'))
rock_button.grid(row=0, column=0, padx=5, pady=5)

paper_button = ttk.Button(button_frame, text="Paper", command=lambda: play_game('Paper'))
paper_button.grid(row=0, column=1, padx=5, pady=5)

scissors_button = ttk.Button(button_frame, text="Scissors", command=lambda: play_game('Scissors'))
scissors_button.grid(row=0, column=2, padx=5, pady=5)

# Customize colors (optional)
root.configure(bg='lightblue')
title_label.configure(background='lightblue', foreground='darkblue')
user_choice_label.configure(background='lightblue', foreground='darkblue')
computer_choice_label.configure(background='lightblue', foreground='darkblue')
result_label.configure(background='lightblue', foreground='darkblue')
button_frame.configure(background='lightblue')

# Pack and display the main window
root.mainloop()
