# Create a program that ask user for a question,
# it will also ask for 4 possible answer (a,b,c,d) and the correct answer. 
# Write the collected data to a text file. 
# Ask another question until the user chose to exit

# Ask the user for a question until exit
while True:

    question_input = input("Enter your question: (Type exit if you wish to exit:)")
    if question_input.lower() == "exit":
        print("Ending program.")
    break

