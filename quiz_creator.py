# Create a program that ask user for a question,
# it will also ask for 4 possible answer (a,b,c,d) and the correct answer. 
# Write the collected data to a text file. 
# Ask another question until the user chose to exit

question_bank = []
# Ask the user for a question until exit
while True:

    question_input = input("Enter your question: (Type exit if you wish to exit:)")

    question_bank.append(question_input)
    if question_input.lower() == "exit":    
        print("Ending program.")
        break # Stops the asking of questions

# Asks for the option to be put as a possible answer 
    letter_a = input("Enter for option A: ")
    letter_b = input("Enter for option B: ")
    letter_c = input("Enter for option C: ")
    letter_d = input("Enter for option D: ")

# Get the correct answer from the possible answers
# Create a dictionary for the possible answers


