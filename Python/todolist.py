import tkinter as tk
from tkinter import messagebox


def add_task():
    task = task_entry.get()
    if task != "":
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")


def delete_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_task_index)
    except:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")


def clear_tasks():
    task_listbox.delete(0, tk.END)


root = tk.Tk()
root.title("To-Do List")


input_frame = tk.Frame(root)
input_frame.pack(pady=10)


task_entry = tk.Entry(input_frame, width=35, font=("Arial", 14))
task_entry.pack(side=tk.LEFT, padx=10)


add_task_button = tk.Button(input_frame, text="Add Task", width=10, command=add_task)
add_task_button.pack(side=tk.LEFT)


task_listbox = tk.Listbox(root, height=10, width=50, font=("Arial", 14))
task_listbox.pack(pady=10)


button_frame = tk.Frame(root)
button_frame.pack(pady=10)


delete_task_button = tk.Button(button_frame, text="Delete Task", width=15, command=delete_task)
delete_task_button.pack(side=tk.LEFT, padx=5)


clear_tasks_button = tk.Button(button_frame, text="Clear Tasks", width=15, command=clear_tasks)
clear_tasks_button.pack(side=tk.LEFT, padx=5)


root.mainloop()
