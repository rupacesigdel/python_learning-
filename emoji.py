import tkinter as tk
from tkinter import messagebox

def display_message():
    messagebox.showinfo("Message", "I love you rupesh")

def on_click(event):
    canvas.create_text(50, 50, text="❤️", font=("Arial", 24), tags="emoji")
    canvas.after(1000, display_message)

root = tk.Tk()
root.title("Love Emoji")

canvas = tk.Canvas(root, width=100, height=100)
canvas.pack()

canvas.bind("<Button-1>", on_click)

root.mainloop()
