import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter import ttk

def add_task():
    task = task_entry.get()
    if task:
        task_tree.insert("", tk.END, values=(task, "Incomplete"))
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

def update_task():
    selected_item = task_tree.selection()
    if selected_item:
        current_task = task_tree.item(selected_item, 'values')[0]
        updated_task = simpledialog.askstring("Update Task", "Update the task:", initialvalue=current_task)
        if updated_task:
            task_tree.item(selected_item, values=(updated_task, task_tree.item(selected_item, 'values')[1]))
    else:
        messagebox.showwarning("Warning", "You must select a task to update.")

def delete_task():
    selected_item = task_tree.selection()
    if selected_item:
        task_tree.delete(selected_item)
    else:
        messagebox.showwarning("Warning", "You must select a task to delete.")

def toggle_status():
    selected_item = task_tree.selection()
    if selected_item:
        current_status = task_tree.item(selected_item, 'values')[1]
        new_status = "Complete" if current_status == "Incomplete" else "Incomplete"
        task_tree.item(selected_item, values=(task_tree.item(selected_item, 'values')[0], new_status))
    else:
        messagebox.showwarning("Warning", "You must select a task to mark as completed.")

# Initialize the main window
root = tk.Tk()
root.title("To-Do List")
root.geometry("500x500")
root.configure(bg='lightblue')

# Title label
title_label = ttk.Label(root, text="To-Do List", font=('Helvetica', 16, 'bold'), background='lightblue', foreground='darkblue')
title_label.pack(pady=10)

# Task entry field
task_entry = ttk.Entry(root, width=30, font=('Helvetica', 12))
task_entry.pack(pady=10)

# Treeview to display tasks
columns = ("Task", "Status")
task_tree = ttk.Treeview(root, columns=columns, show='headings', selectmode='browse')
task_tree.heading("Task", text="Task")
task_tree.heading("Status", text="Status")
task_tree.column("Task", width=300)
task_tree.column("Status", width=100)
task_tree.pack(pady=10, fill=tk.BOTH, expand=True)

# Scrollbar for the treeview
scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=task_tree.yview)
task_tree.configure(yscrollcommand=scrollbar.set)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Buttons for add, update, delete, and toggle status
button_frame = tk.Frame(root, bg='lightblue')
button_frame.pack(pady=10)

add_button = ttk.Button(button_frame, text="Add Task", command=add_task)
add_button.grid(row=0, column=0, padx=5)

update_button = ttk.Button(button_frame, text="Update Task", command=update_task)
update_button.grid(row=0, column=1, padx=5)

delete_button = ttk.Button(button_frame, text="Delete Task", command=delete_task)
delete_button.grid(row=0, column=2, padx=5)

toggle_button = ttk.Button(button_frame, text="mark as completed", command=toggle_status)
toggle_button.grid(row=0, column=3, padx=5)

# Pack and display the main window
root.mainloop()
