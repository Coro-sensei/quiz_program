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
window_width = 1500
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
button_font =("Georgia", 16, "bold")

# Central frame to hold the widgets
central_frame =  tk.Frame(window_root)
central_frame.grid(row = 0, column = 0)

# Do the code for the quiz maker itself 
# Input questions
question_label = tk.Label(central_frame, text = "Enter your question: ", font = label_font)
question_label.grid(row = 0, column = 0, sticky = "e")
question_entry = tk.Entry(central_frame, width = 80, font = entry_font)
question_entry.grid(row = 0, column = 1)

# Input 4 possible answers 
# For option A
opt_a_label = tk.Label(central_frame, text = "Option A:", font = label_font)
opt_a_label.grid(row = 1, column = 0, sticky = "e")
opt_a_entry = tk.Entry(central_frame, width = 80, font = entry_font)
opt_a_entry.grid(row = 1, column = 1)

# For Option B 
opt_b_label = tk.Label(central_frame, text = "Option B:", font = label_font)
opt_b_label.grid(row = 2, column = 0, sticky = "e")
opt_b_entry = tk.Entry(central_frame, width = 80, font = entry_font)
opt_b_entry.grid(row = 2, column = 1)

# For Option C
opt_c_label = tk.Label(central_frame, text = "Option C:", font = label_font)
opt_c_label.grid(row = 3, column = 0, sticky = "e")
opt_c_entry = tk.Entry(central_frame, width = 80, font = entry_font)
opt_c_entry.grid(row = 3, column = 1)

# For Option D
opt_d_label = tk.Label(central_frame, text = "Option D:", font = label_font)
opt_d_label.grid(row = 4, column = 0, sticky = "e")
opt_d_entry = tk.Entry(central_frame, width = 80, font = entry_font)
opt_d_entry.grid(row = 4, column = 1)

# The correct answer
correct_answer_label = tk.Label(central_frame, text = "Correct answer (a/b/c/d): ", font = label_font)
correct_answer_label.grid(row = 5, column = 0, sticky = "e")
correct_answer_entry = tk.Entry(central_frame, width = 10, font = entry_font)
correct_answer_entry.grid(row = 5, column = 1, sticky = "w") 

# Submit the inputs 
def submit_question():
    question = question_entry.get()
    a = opt_a_entry.get()
    b = opt_b_entry.get()
    c = opt_c_entry.get()
    d = opt_d_entry.get()
    correct = correct_answer_entry.get().lower() 

    if correct not in ['a', 'b', 'c', 'd']:
        messagebox.showerror("Invalid data", "Please put the correct answer that is within the options submitted")
        return
    if not all ([question, a, b, c, d]):
        messagebox.showerror("Missing inputs, please fill all the entry boxes")
        return

# Write the data to a text file
    with open("quiz_maker_data.txt", "a") as file:
        file.write(f"Question: {question}\n")
        file.write(f"a) {a}\n")
        file.write(f"b) {b}\n")
        file.write(f"c) {c}\n")
        file.write(f"d) {d}\n")
        file.write(f"The correct answer: {correct}\n")
        file.write("-" * 40 + "\n")
    messagebox.showinfo("Success", "Question is saved in a text file.")

# Delete the all the entry
    question_entry.delete(0, tk.END)
    opt_a_entry.delete(0, tk.END)
    opt_b_entry.delete(0, tk.END)
    opt_c_entry.delete(0, tk.END)
    opt_d_entry.delete(0, tk.END)
    correct_answer_entry.delete(0, tk.END)

# Submit button for the def function to work
submit_button = tk.Button(central_frame, text = "Submit", font = button_font, command = submit_question)
submit_button.grid(row = 6, column = 1, sticky = "e")

# Delete button using def function
def clear_entry():
    question_entry.delete(0, tk.END)
    opt_a_entry.delete(0, tk.END)
    opt_b_entry.delete(0, tk.END)
    opt_c_entry.delete(0, tk.END)
    opt_d_entry.delete(0, tk.END)
    correct_answer_entry.delete(0, tk.END)
clear_button = tk.Button(central_frame, text = "Clear all entry", font = button_font, command = clear_entry)
clear_button.grid(row = 6, column = 0, sticky = "e")

# Run the app
window_root.mainloop()