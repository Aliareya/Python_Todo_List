import tkinter as tk
from tkinter import messagebox

# ---------------- Window ----------------
root = tk.Tk()
root.title("To-Do List")
root.geometry("420x500")
root.config(bg="#133b63")

# ---------------- Functions ----------------
def add_task():
    task = entry.get().strip()
    if task:
        listbox.insert(tk.END, f"• {task}")
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty")

def delete_task():
    try:
        listbox.delete(listbox.curselection())
    except:
        messagebox.showwarning("Warning", "Select a task first")

# ---------------- Title ----------------
title = tk.Label(
    root,
    text="My Tasks",
    font=("Segoe UI", 20, "bold"),
    bg="#f4f6f8",
    fg="#333"
)
title.pack(pady=15)

# ---------------- Input Area ----------------
frame = tk.Frame(root, bg="#f4f6f8")
frame.pack(pady=10)

entry = tk.Entry(
    frame,
    font=("Segoe UI", 12),
    width=22,
    relief="solid",
    bd=1
)
entry.grid(row=0, column=0, padx=5)

add_btn = tk.Button(
    frame,
    text="Add",
    font=("Segoe UI", 11),
    bg="#4CAF50",
    fg="white",
    width=8,
    relief="flat",
    command=add_task
)
add_btn.grid(row=0, column=1, padx=5)

# ---------------- Task List ----------------
listbox = tk.Listbox(
    root,
    font=("Segoe UI", 12),
    width=38,
    height=12,
    bg="white",
    fg="#333",
    selectbackground="#2196F3",
    activestyle="none",
    relief="solid",
    bd=1
)
listbox.pack(pady=15)

# ---------------- Delete Button ----------------
del_btn = tk.Button(
    root,
    text="Delete Selected Task",
    font=("Segoe UI", 11),
    bg="#f44336",
    fg="white",
    relief="flat",
    width=25,
    command=delete_task
)
del_btn.pack(pady=10)

# ---------------- Run ----------------
root.mainloop()
