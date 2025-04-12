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
window_width = 800
window_height = 800

# Get screen dimensions 
screen_window_width = window_root.winfo_screenwidth()
screen_window_height = window_root.winfo_screenheight()

# Get the x and y for the window to be centered
x = (screen_window_width // 2) - (window_width // 2)
y = (screen_window_height // 2) - (window_height // 2)


# Do the code for the quiz maker itself 
# Input questions
# Input 4 possible answers 
# Input the correct answer 
# Write the data to a text file