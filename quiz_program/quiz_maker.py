# Create a program that ask user for a question,
# It will also ask for 4 possible answer (a,b,c,d) and the correct answer. 
# Write the collected data to a text file. Ask another question until the user chose to exit.

# Make the GUI 

import tkinter as tk  # The library used 
from tkinter import messagebox

# Main window of the GUI
window_root = tk.Tk()
window_root.title("Quiz Maker")

# Set the window dimensions
window_width = 1800
window_height = 800

# Get screen dimensions 
screen_window_width = window_root.winfo_screenwidth()
screen_window_height = window_root.winfo_screenheight()

# Get the x and y for the window to be centered
x = (screen_window_width // 2) - (window_width // 2)
y = (screen_window_height // 2) - (window_height // 2)

# Set the center for the window
window_root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Font style 
label_font = ("Georgia", 16)
entry_font = ("Georgia", 14)

# Central frame to hold the widgets
central_frame =  tk.Frame(window_root)
central_frame.grid(row = 0, column = 0)

# Do the code for the quiz maker itself 
# Input questions
question_label = tk.Label(window_root, text = "Enter your question: ", font = label_font)
question_label.grid(row = 0, column = 0, sticky = "w")
question_entry = tk.Entry(window_root, width = 100, font = entry_font)
question_entry.grid(row = 0, column = 1)


# Input 4 possible answers 
# Input the correct answer 
# Write the data to a text file
# Run the app
window_root.mainloop()