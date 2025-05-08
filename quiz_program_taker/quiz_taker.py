# Create a  quiz taker program 
# Create a GUI for the program
# Use the text file of quiz maker

# Make the GUI
import tkinter as tk 
from tkinter import messagebox
import os 
from PIL import Image, ImageTk

quiz_data = []

if os.path.exists("quiz_maker_data.txt"):
    with open("quiz_maker_data.txt", "r") as f:
        blocks = f.read().strip().split("-" * 40)
        for blocks in blocks:
            lines = blocks.strip().split("\n")
            if len(lines) < 6:
                continue