import random

#Print the banner
print("Arithmetic Quiz!")
print("Level 1: 1-3, Level 2: 1-6")
print("Level 3: 1-9, Level 4: 1-12")

#Get the inputs.
level = int(input("\nEnter Level (1) through (4): "))
num_questions = int(input("How many questions?: "))

#Determine the number range based on the level.
if level == 1:
    num_range = 3
elif level == 2:
    num_range = 6
elif level == 3:
    num_range = 9
else:
    num_range = 12

#Define a function to check if the answer is correct.
def check_answer(num1, operation, num2, user_answer):
    correct_answer = eval(f"{num1} {operation} {num2}")
    return correct_answer == user_answer

#Set default values.
num_correct = 0

#Ask the questions and check answers.
for i in range(num_questions):
    num1 = random.randint(1, num_range)
    num2 = random.randint(1, num_range)
    operation = random.choice("+-*")

    #Print the question
    print("What is", str(num1), operation, str(num2), "?: ", end="")
    
    #Get the user input and check the answer.
    user_answer = int(input())
    if check_answer(num1, operation, num2, user_answer):
        num_correct += 1

# Calculate and print the final score
score = (num_correct / num_questions) * 100
print("\nYour final score is: ", str(format(score, ".2f")) + "%")
