# Create a  quiz taker program 
# Create a GUI for the program
# Use the text file of quiz maker

# Make the GUI
import tkinter as tk 
from tkinter import messagebox
import os 
from PIL import Image, ImageTk

# Image handler
def image_loader(path, size = None):
    try: 
        image = Image.open(path)
        if size:
            image = image.resize(size, Image.ANTIALIAS)
        return ImageTk.PhotoImage(image)
    
    except Exception as error:
        print(f"Image failed for {path}: {"error"} ")

        return None

# Reads and finds the text file
quiz_data = []

if os.path.exists("quiz_maker_data.txt"):
    with open("quiz_maker_data.txt", "r") as f:
        blocks = f.read().strip().split("-" * 40)
        for blocks in blocks:
            lines = blocks.strip().split("\n")
            if len(lines) < 6:
                continue

        question_lines = lines[0][len("Question: ")].strip()

        options = {
            "letter_a": lines[1][4:].strip(),
            "letter_b": lines[2][4:].strip(),
            "letter_c": lines[3][4:].strip(),
            "letter_d": lines[4][4:].strip(),
        
        }

        correct = lines[5].split(":")[-1].strip().lower()
        quiz_data.append((question_lines,options,correct))

else:
    messagebox.showerror("Quiz data not found, Run the quiz maker first to make the quiz data.")
    exit()

# window size of GUI 
window_root = tk.Tk()
window_root.title("Pokemon Quiz Taker")
window_root.geometry("1600x800")
window_root.resizable(False, False)

# Background 
bg_photo = 