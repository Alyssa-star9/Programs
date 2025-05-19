# AD-1051350-quiz_v2.py
#
# Description: This program is an updated version of the Elementary_quiz.py program.
#              It asks the user to select a level of difficulty and the number of questions. 
#              The program uses while loops to ask the user for input and validate it.
#              It generates random numbers and operations, and checks the user's answers.
#              The program also calculates the score and prints it at the end.

import random # To generate random numbers for the quiz

# Print the banner
print("Arithmetic Quiz!")
print("Level 1: 1-3, Level 2: 1-6")
print("Level 3: 1-9, Level 4: 1-12")

# Get the inputs and validate them with a while loop.
asking = True # Sentinel variable to continue the loop

while asking:
    try:
        level = int(input("\nEnter Level (1) through (4): "))
        if (level < 1) or (level > 4):
            print("Please enter a valid integers only")
            continue
        # Get the number of questions to ask.
        num_questions = int(input("How many questions?: "))
        if (num_questions <= 0):
            print("Please enter valid integers only")
    except:
        print("Please enter valid integers only")
        continue

    asking = False # All inputs are valid, so we can exit the loop.

# Determine the number range based on the level.
if level == 1:
    num_range = 3
elif level == 2:
    num_range = 6
elif level == 3:
    num_range = 9
else:
    num_range = 12

# Set default values.
num_correct = 0
question_num = 0 

# Ask the questions and check answers.
while (question_num < num_questions):
    num1 = random.randint(1, num_range)
    num2 = random.randint(1, num_range)
    operation = random.choice("+-*")

    valid_input = False  # Sentinel for validating input
    while not valid_input:
        try:
            user_input = input(f"What is {num1} {operation} {num2} ?: ")
            user_answer = int(user_input)

            # Check if the user input is the correct answer.
            if (operation == "+"):
                correct_answer = num1 + num2
            elif (operation == "-"):
                correct_answer = num1 - num2
            else:
                correct_answer = num1 * num2

            if (user_answer == correct_answer):
                num_correct += 1

            valid_input = True  # Valid input received
        except:
            print("Please enter valid integers only")

    question_num += 1  # Only increment after valid input

# Calculate and print the final score
score = (num_correct / num_questions) * 100
print(f"\nYour final score is: {score:.2f}%")