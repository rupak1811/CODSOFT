import tkinter as tk
from tkinter import ttk

def button_click(value):
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current_text + str(value))

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Initialize the main window
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")
root.configure(bg='black')

# Entry field
entry = ttk.Entry(root, font=('Helvetica', 18), justify='right')
entry.pack(fill=tk.BOTH, ipadx=8, ipady=8, padx=8, pady=8)

# Button frame
button_frame = tk.Frame(root, bg='black')
button_frame.pack(expand=True, fill=tk.BOTH)

# Button configuration
button_config = {'font': ('Helvetica', 14), 'bg': 'white', 'fg': 'black', 'bd': 0, 'highlightthickness': 0, 'activebackground': 'black', 'activeforeground': 'white'}

# Buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3)
]

for (text, row, col) in buttons:
    if text == '=':
        button = tk.Button(button_frame, text=text, command=calculate, **button_config)
    else:
        button = tk.Button(button_frame, text=text, command=lambda t=text: button_click(t), **button_config)
    button.grid(row=row, column=col, sticky='nsew', padx=1, pady=1)

# Clear button
clear_button = tk.Button(button_frame, text='C', command=clear, **button_config)
clear_button.grid(row=0, column=0, columnspan=4, sticky='nsew', padx=1, pady=1)

# Configure grid
for i in range(1, 5):
    button_frame.grid_rowconfigure(i, weight=1)
    button_frame.grid_columnconfigure(i, weight=1)

# Run the main loop
root.mainloop()
