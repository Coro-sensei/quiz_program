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
            image = image.resize(size, Image.Resampling.LANCZOS)
        return ImageTk.PhotoImage(image)
    
    except Exception as error:
        print(f"Image failed for {path}: {"error"} ")

        return None

# Reads and finds the text file
def load_quiz_data():
    quiz_data = []
    if not os.path.exists("quiz_maker_data.txt"):
        messagebox.showerror("Error", "Quiz data not found. Run quiz maker first.")
        exit()

    with open("quiz_maker_data.txt", "r") as f:
        blocks = f.read().strip().split("\n" + "-" * 40 + "\n")
        
        for block in blocks:
            lines = [line.strip() for line in block.split("\n") if line.strip()]
            if len(lines) < 6:
                continue

            try:
                # Extract question from first line
                question = lines[0].split("Question: ")[1].strip()
                
                # Extract options (a-d)
                options = {
                    'a': lines[1][3:].strip(),  # Skip "a) "
                    'b': lines[2][3:].strip(),
                    'c': lines[3][3:].strip(),
                    'd': lines[4][3:].strip()
                }
                
                # Extract correct answer
                correct = lines[5].split(": ")[1].strip().lower()
                
                if correct in options:
                    quiz_data.append((question, options, correct))
                else:
                    print(f"Skipping invalid question: {question[:30]}...")

            except (IndexError, KeyError) as e:
                print(f"Error parsing block: {e}")
                continue

    return quiz_data

quiz_data = load_quiz_data()
if not quiz_data:
    messagebox.showerror("Error", "No valid questions found in quiz data.")
    exit()


# window size of GUI 
window_root = tk.Tk()
window_root.title("Pokemon Quiz Taker")
window_root.geometry("1600x800")
window_root.resizable(False, False)

# Background 
bg_photo = image_loader ("pokeball_bg.jpeg",(1600,800))
if bg_photo:
    tk.Label(window_root, image = bg_photo).place(x = 0, y = 0, relwidth = 1, relheight = 1)
else:
    window_root.configure(bg = "yellow")

# Quiz Status
current_question = [0]
score = [0]
selected_answer = tk.StringVar()

frame = tk.Frame(window_root, bg = "yellow", width = 1200, height = 600)
frame.place(relx = 0.5, rely = 0.5, anchor = "center")

question_label = tk.Label(frame, font = ("Arial", 20), bg = "yellow", wraplength = 1000, justify = "left")

question_label.pack(anchor = "w")

radio_buttons = {}
for key in ["a", "b", "c", "d"]:
    rad_but = tk.Radiobutton(frame, variable = selected_answer, value = key, font = ("Arial", 16), bg = "yellow", anchor = "w", justify = "left")

    rad_but.pack(anchor = "w")
    radio_buttons[key] = rad_but

# Labels for feedback and score
status_label = tk.Label(frame, font =("Arial, 16"), bg = "yellow", fg = "lightyellow")
status_label.pack()

# Load the next question
def load_question():
    global current_question, score 

    if current_question < len(quiz_data):
        question_lines, options, _ = quiz_data[current_question]
        question_label.config(text = f"Question{current_question + 1}: {question_lines}")
        for key in options:
            radio_buttons[key].config(text = f"{key.upper()}){options[key]}")
        selected_answer.set("")
        status_label.config(text = "")
    
    else:
        question_label.config(text = "Quiz Finished")

        for rad_but in radio_buttons.values():
            rad_but.pack_forget()
    submit_button.pack_forget()
    status_label.config(text = f"Your score: {score}/{len(quiz_data)}")

# Submit answer
def submit_answer():
    global current_question, score
    if selected_answer.get() == "":
        messagebox.showwarning("No Answer", "Please select an option.")
        return
    _, _, correct = quiz_data[current_question]
    if selected_answer.get() == correct:
        score += 1

    current_question += 1
    if current_question < len(quiz_data):
        load_question()
    else:
        load_question() 

submit_button = tk.Button(frame, text = "Submit", font =("Arial", 16, "bold"), command = submit_answer)
submit_button.pack(anchor = "e")


window_root.mainloop()


