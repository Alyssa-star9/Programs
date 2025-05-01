# AD-1051350-rand_num.py
#
# Description: This program comes up with a random number between 1 and 100, 
#              and then asks the user to guess the number. If the user is wrong,
#              the program tells them if they are too high or too low. The program
#              continues until the user guesses the number correctly or the user runs
#              out of guesses (based on difficulty level). If the user wins, the program
#              tells them how many guesses it took. If the user loses, the program
#              tells them the correct number.

import random # To generate random numbers

# Set initial while loop for the game.
asking = True # Sentinel variable to continue the loop

while asking:
    # Game instructions
    print("Welcome to the Guessing Game!\n")
    print("I have selected a random number between 1 and 100.")
    print("You have to guess the number in a limited number of attempts.")
    print("If you guess too high, I will tell you to guess lower.")
    print("If you guess too low, I will tell you to guess higher.")
    print("If you guess the number, I will tell you how many attempts it took.\n")
    print("Let's get started!\n")

    # Select a difficulty level.
    level = input("Select a difficulty level (easy, medium, hard): ")

    # Generate a random number between 1 and 100.
    rand_num = random.randint(1, 100)

    # Set the number of attempts based on the difficulty level.
    attempts = 0 # Initialize attempts
    user_guess = 0 # Initialize user_guess

    if (level == "easy"):
        while (attempts != 15) and (rand_num != user_guess):
            try:
                user_guess = int(input("\nEnter your guess (1-100): "))
                attempts += 1 # Increment attempts
                if (attempts < 15):
                    if (user_guess < rand_num):
                        print("Too low! Try again.")
                    elif (user_guess > rand_num):
                        print("Too high! Try again.")
                    elif (user_guess == rand_num):
                        print(f"\nCongratulations! You guessed the number {rand_num} in {attempts} attempts.")
                        user_guess == rand_num
                elif (user_guess == rand_num):
                    print(f"\nCongratulations! You guessed the number {rand_num} in {attempts} attempts.")
                    user_guess == rand_num # Set user_guess to rand_num to exit the loop
            except:
                print("That was not a valid input. Please enter a number between 1 and 100.")
                attempts -= 1 # Decrement attempts if input is invalid

    elif (level == "medium"):
        while (attempts != 10) and (rand_num != user_guess):
            try:
                user_guess = int(input("\nEnter your guess (1-100): "))
                attempts += 1 # Increment attempts
                if (attempts < 10):
                    if (user_guess < rand_num):
                        print("Too low! Try again.")
                    elif (user_guess > rand_num):
                        print("Too high! Try again.")
                    elif (user_guess == rand_num):
                        print(f"\nCongratulations! You guessed the number {rand_num} in {attempts} attempts.")
                        user_guess == rand_num
                elif (user_guess == rand_num):
                    print(f"\nCongratulations! You guessed the number {rand_num} in {attempts} attempts.")
                    user_guess == rand_num # Set user_guess to rand_num to exit the loop
            except:
                print("That was not a valid input. Please enter a number between 1 and 100.")
                attempts -= 1

    elif (level == "hard"):
        while (attempts != 5) and (rand_num != user_guess):
            try:
                user_guess = int(input("\nEnter your guess (1-100): "))
                attempts += 1 # Increment attempts
                if (attempts < 5):
                    if (user_guess < rand_num):
                        print("Too low! Try again.")
                    elif (user_guess > rand_num):
                        print("Too high! Try again.")
                    elif (user_guess == rand_num):
                        print(f"\nCongratulations! You guessed the number {rand_num} in {attempts} attempts.")
                        user_guess == rand_num
                elif (user_guess == rand_num):
                    print(f"\nCongratulations! You guessed the number {rand_num} in {attempts} attempts.")
                    user_guess == rand_num # Set user_guess to rand_num to exit the loop
            except:
                print("That was not a valid input. Please enter a number between 1 and 100.")
                attempts -= 1

    # If the user runs out of attempts, tell them the correct number.
    if (attempts == 5) and (level == "hard"):
        print(f"\nSorry, you have run out of attempts. The correct number was {rand_num}.")
    elif (attempts == 10) and (level == "medium"):
        print(f"\nSorry, you have run out of attempts. The correct number was {rand_num}.")
    elif (attempts == 15) and (level == "easy"):
        print(f"\nSorry, you have run out of attempts. The correct number was {rand_num}.")

    # Ask the user if they want to play again.
    play_again = input("\nDo you want to play again? (y/n): ")
    if (play_again != "y"):
        asking = False # Exit the loop
        print("\nThanks for playing! Goodbye!")