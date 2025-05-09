# Create a  quiz taker program 
# Create a GUI for the program
# Use the text file of quiz maker

import tkinter as tk 
from tkinter import messagebox
import os 
from PIL import Image, ImageTk
import tkinter.font as tkFont


def image_loader(path, size = None):
    try: 
        image = Image.open(path)
        if size:
            image = image.resize(size, Image.Resampling.LANCZOS)
        return ImageTk.PhotoImage(image)
    except Exception as error:
        print(f"Image load failed: {error}")
        return None

# Quiz data loader
def load_quiz_data():
    quiz_data = []
    if not os.path.exists("quiz_maker_data.txt"):
        messagebox.showerror("Error", "Run quiz maker first to create questions!")
        exit()

    with open("quiz_maker_data.txt", "r") as f:
        content = f.read().strip()
        blocks = content.split("\n" + "-" * 40 + "\n")
        
        for block in blocks:
            lines = [line.strip() for line in block.split("\n") if line.strip()]
            if len(lines) < 6:
                continue

            try:
                # Extract question (first line)
                question = lines[0].split("Question: ")[1]
                
                # Extract options (next 4 lines)
                options = {
                    'a': lines[1][3:].strip(),  # Remove "a) " prefix
                    'b': lines[2][3:].strip(),
                    'c': lines[3][3:].strip(),
                    'd': lines[4][3:].strip()
                }
                
                # Get correct answer (last line)
                correct = lines[5].split(": ")[1].strip().lower()
                
                if correct in ['a', 'b', 'c', 'd']:
                    quiz_data.append((question, options, correct))
                else:
                    print(f"Skipping invalid answer in: {question[:50]}...")

            except Exception as e:
                print(f"Error parsing question: {e}")
                continue

    return quiz_data

quiz_data = load_quiz_data()
if not quiz_data:
    messagebox.showerror("Error", "No valid questions found!")
    exit()

# Create GUI
window_root = tk.Tk()
window_root.title("Pokemon Quiz Taker")
window_root.geometry("1600x800")
window_root.resizable(False, False)

# Fonts
try:
    title_font = tkFont.Font(family = "Pokemon Hollow", size = 48)
    question_font = tkFont.Font(family = "Kenney Mini Square", size = 20)
    option_font = tkFont.Font(family = "Kenney Mini Square", size=16)
    button_font = tkFont.Font(family = "Kenney Mini Square", size=18, weight = "bold")

except:
    # If font not in system
    title_font = tkFont.Font(family = "Helvetica", size = 36, weight = "bold")
    question_font = tkFont.Font(family = "Arial", size = 18)
    option_font = tkFont.Font(family = "Arial", size = 14)
    button_font = tkFont.Font(family = "Arial", size = 16, weight="bold")

# Background
bg_photo = image_loader("pokeball_bg.jpeg", (1600, 800))
if bg_photo:
    tk.Label(window_root, image = bg_photo).place(x = 0, y = 0, relwidth = 1, relheight = 1)
else:
    window_root.configure(bg="yellow")

# Quiz state
current_question = 0
score = 0
selected_answer = tk.StringVar()

# Main frame
frame = tk.Frame(window_root, bg = "yellow", width = 1200, height = 600)
frame.place(relx = 0.5, rely = 0.5, anchor="center")

# Question display
question_label = tk.Label(frame, font = question_font, bg = "yellow", 
                        wraplength = 1000, justify = "left")
question_label.pack(anchor="w", pady = 20)

# Answer options
radio_buttons = {}
for letter in ['a', 'b', 'c', 'd']:
    rb = tk.Radiobutton(
        frame,
        text = "",
        variable = selected_answer,
        value = letter,
        font = button_font,
        bg = "yellow",
        anchor = "w",
        justify = "left"
    )
    rb.pack(anchor = "w", fill = 'x', padx = 20)
    radio_buttons[letter] = rb

# Score display
status_label = tk.Label(frame, font = option_font, bg = "yellow", fg = "black")
status_label.pack(pady = 20)

def show_question():
    global current_question
    if current_question < len(quiz_data):
        question, options, _ = quiz_data[current_question]
        question_label.config(text=f"Question {current_question+1}: {question}")
        
        for letter in ['a', 'b', 'c', 'd']:
            radio_buttons[letter].config(text = f"{letter.upper()}) {options[letter]}")
        
        selected_answer.set("")
        status_label.config(text = f"Score: {score}/{len(quiz_data)}")
    else:
        end_quiz()

def end_quiz():
    question_label.config(text="Quiz Completed!")
    for rb in radio_buttons.values():
        rb.pack_forget()
    submit_button.pack_forget()
    status_label.config(text = f"Final Score: {score}/{len(quiz_data)}")

def check_answer():
    global current_question, score
    if not selected_answer.get():
        messagebox.showwarning("Warning", "Please select an answer!")
        return
    
    _, _, correct = quiz_data[current_question]
    if selected_answer.get() == correct:
        score += 1
    
    current_question += 1
    show_question()

# Submit button
submit_button = tk.Button(frame, text="Submit Answer", font= button_font,
                        command=check_answer)
submit_button.pack(anchor="e", pady=20)

show_question()
window_root.mainloop()