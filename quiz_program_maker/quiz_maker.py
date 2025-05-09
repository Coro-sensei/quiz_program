# Create a program that ask user for a question,
# It will also ask for 4 possible answer (a,b,c,d) and the correct answer. 
# Write the collected data to a text file. Ask another question until the user chose to exit.

# Make the GUI 
import os
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import tkinter.font as tkFont

# Main window of the GUI
window_root = tk.Tk()
window_root.title("Pokemon Quiz Maker")

# Set the window dimensions
window_width = 1600
window_height = 800
window_root.resizable(False, False)

# Center the window
screen_width = window_root.winfo_screenwidth()
screen_height = window_root.winfo_screenheight()
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
window_root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Image handling improvements
def load_image(path, size = None):
    try:
        image = Image.open(path)
        if size:
            image = image.resize(size, Image.Resampling.LANCZOS)
        return ImageTk.PhotoImage(image)
    except Exception as e:
        messagebox.showerror("Image Error", f"Failed to load {path}: {str(e)}")
        return None

# Background with error handling
bg_photo = load_image("pokeball_bg.jpeg", (window_width, window_height))
if bg_photo:
    tk.Label(window_root, image = bg_photo).place(x=0, y=0)
else:
    window_root.config(bg="yellow")

# Font handling with fallbacks
try:
    label_font = tkFont.Font(family = "Kenney Mini Square", size = 16)
    entry_font = tkFont.Font(family = "Kenney Mini Square", size = 14)
    button_font = tkFont.Font(family = "Kenney Mini Square", size = 16, weight = "bold")
except:
    label_font = tkFont.Font(size = 16)
    entry_font = tkFont.Font(size = 14)
    button_font = tkFont.Font(size = 16, weight = "bold")

# Central frame
central_frame = tk.Frame(window_root, bg = "yellow")
central_frame.place(relx = 0.5, rely = 0.5, anchor = "center")

# Title image with better error handling
title_image = load_image("pokeball_title.png", (550, 250))
if title_image:
    title_label = tk.Label(window_root, image = title_image, bg = "yellow")
    title_label.place(relx = 0.5, rely = 0.2, anchor = "center")
else:
    title_label = tk.Label(window_root, text = "Pokemon Quiz Maker", 
                        font = ("Kenny Mini Square", 24, "bold"), bg = "yellow")
    title_label.place(relx = 0.5, rely = 0.2, anchor = "center")

# Widget creation functions
def create_label(text, row):
    return tk.Label(central_frame, text = text, font = label_font, bg = "yellow").grid(row = row, column = 0, sticky = "e")

def create_entry(row):
    entry = tk.Entry(central_frame, width = 80, font = entry_font)
    entry.grid(row = row, column = 1)
    return entry

# Create input fields
question_label = create_label("Enter your question:", 0)
question_entry = create_entry(0)

opt_a_label = create_label("Option A:", 1)
opt_a_entry = create_entry(1)

opt_b_label = create_label("Option B:", 2)
opt_b_entry = create_entry(2)

opt_c_label = create_label("Option C:", 3)
opt_c_entry = create_entry(3)

opt_d_label = create_label("Option D:", 4)
opt_d_entry = create_entry(4)

# Correct answer input
correct_answer_label = create_label("Correct answer (a/b/c/d):", 5)
correct_answer_entry = tk.Entry(central_frame, width=10, font = entry_font)
correct_answer_entry.grid(row = 5, column = 1, sticky = "w")

# Submission handling
def submit_question():
    # Get all values
    entries = [
        question_entry.get(),
        opt_a_entry.get(),
        opt_b_entry.get(),
        opt_c_entry.get(),
        opt_d_entry.get(),
        correct_answer_entry.get().lower()
    ]
    
    # Validation
    if not all(entries):
        messagebox.showerror("Error", "Please fill in all fields")
        return
    
    if entries[5] not in ['a', 'b', 'c', 'd']:
        messagebox.showerror("Error", "Correct answer must be a, b, c, or d")
        return

    # Save to file
    try:
        with open("quiz_maker_data.txt", "a") as f:
            f.write(f"Question: {entries[0]}\n")
            f.write(f"a) {entries[1]}\n")
            f.write(f"b) {entries[2]}\n")
            f.write(f"c) {entries[3]}\n")
            f.write(f"d) {entries[4]}\n")
            f.write(f"Correct Answer: {entries[5]}\n")
            f.write("-" * 40 + "\n")
        messagebox.showinfo("Success", "Question saved successfully!")
        
        # Clear entries
        for entry in [question_entry, opt_a_entry, opt_b_entry, 
                    opt_c_entry, opt_d_entry, correct_answer_entry]:
            entry.delete(0, tk.END)
            
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save question: {str(e)}")

# Buttons
submit_button = tk.Button(central_frame, text = "Submit", font=button_font, command=submit_question)
submit_button.grid(row = 6, column = 1, sticky = "e")

clear_button = tk.Button(central_frame, text="Clear All", font=button_font, 
                        command=lambda: [e.delete(0, tk.END) for e in [
                            question_entry, opt_a_entry, opt_b_entry,
                            opt_c_entry, opt_d_entry, correct_answer_entry
                        ]])
clear_button.grid(row = 6, column = 0, sticky = "e")

window_root.mainloop()