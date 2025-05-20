# File Name: AD-1051350-game.py
# Description: "Game Dice Generator"
#              This program generates a random number between 1 and 6, simulating a dice roll.
#              It then asks the user if they want to roll again. The program continues until the user chooses to stop.
#              The results are printed.


# Import random module for generating random numbers
import random

#function to return valid integer
def get_int():
    """This function asks for the maximum possible value to generate,
    and the number of times player wants to roll the dice
    Args: none
    Returns: valid input >0
    """
    asking = True # sentinal variable
    while asking:
        try:
            max_num = int(input("\nEnter the maximum value to generate (>1): "))
            rolls = int(input("Enter the number of times you want to roll the \
die: "))
            if (max_num < 1) or (rolls < 1):
                print("Invalid input. Please enter a number >1.")
            else:
                asking = False
        except:
            print("Invalid input. Please enter an integer >1.")
    return max_num, rolls
    
#function to generate random numbers
def rand_nums(max_num, rolls):
    """This function generates a list of random numbers
    up to the max value, based on the number of dice rolls
    Args: max_num and rolls (from previous function)
    Returns: list of random dice rolls
    """
    random_list = []
    for i in range(1, rolls + 1):
        num = random.randint(1, max_num)
        random_list.append(num)
    return random_list
    
#function to run the damn program
def main():
    """This function uses a while loop to run the actual program
    Args: none
    Returns: none
    """
    playing = True # sentinal variable
    while playing:
        # Print the welcome banner and the instructions
        print("\n*** Welcome to the Game Dice Generator ***")
        print("\nINSTRUCTIONS:")
        print("When prompted, enter the maximum possible value to generate")
        print("and how many times you wish to roll that die.")
        print("You will get a list of numbers that you rolled!")
        
        maximum, num_rolls = get_int()
        if (maximum > 1) and (num_rolls > 1):
            rand_list = rand_nums(maximum, num_rolls)
            print(f"\nYou rolled: {rand_list}")
        
        # clause to exit the program
        play_again = input("\nPlay again? (y/n): ")
        if play_again != "y":
            playing = False
            print("\nThank you. Have a great day!\n")
        
# run the main program
main()