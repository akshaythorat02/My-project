# -*- coding: utf-8 -*-ss
import tkinter as tk
from tkinter import messagebox as ms
from tkinter.ttk import *
from PIL import Image, ImageTk
from subprocess import call
import os

# --- Functions ---
def login():
    try:
        call(["python", "login1.py"])
    except Exception as e:
        ms.showerror("Error", f"Login failed: {e}")

def register():
    try:
        call(["python", "registration.py"])
    except Exception as e:
        ms.showerror("Error", f"Registration failed: {e}")

# --- Main Window ---
root = tk.Tk()
root.title("Yoga Pose Detection Using Machine Learning")

# Full screen size
screen_w, screen_h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry(f"{screen_w}x{screen_h}+0+0")
root.configure(background="skyblue")

# --- Background Image ---
try:
    image = Image.open("y1.jpg")
    image = image.resize((screen_w, screen_h), Image.LANCZOS)
    background_image = ImageTk.PhotoImage(image)
    background_label = tk.Label(root, image=background_image)
    background_label.place(x=0, y=93)
except Exception as e:
    ms.showerror("Image Load Error", f"Could not load background image: {e}")

# --- Title Label ---
title_label = tk.Label(root, text="Yoga Pose Detection Using Machine Learning",
                       width=50, background="skyblue", height=2,
                       font=("Times New Roman", 19, "bold"))
title_label.place(x=0, y=15)

# --- Welcome Label ---
welcome_label = tk.Label(root,
                         text="......Welcome to Yoga Pose Detection System ......",
                         width=85, height=3, background="skyblue",
                         foreground="black", font=("Times New Roman", 22, "bold"))
welcome_label.place(x=0, y=screen_h - 100)

# --- Buttons ---
login_btn = tk.Button(root, text="Login", command=login,
                      width=9, height=2, bd=0, background="skyblue",
                      foreground="black", font=("Times New Roman", 14, "bold"))
login_btn.place(x=screen_w - 220, y=18)

register_btn = tk.Button(root, text="Register", command=register,
                         width=9, height=2, bd=0, background="skyblue",
                         foreground="black", font=("Times New Roman", 14, "bold"))
register_btn.place(x=screen_w - 110, y=18)

# --- Mainloop ---
root.mainloop()


