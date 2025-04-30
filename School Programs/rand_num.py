# AD-1051350-rand_num.py
#
# Description: This program asks the user how many random numbers they want to generate,
#              then generates that many random numbers between a range the user specifies.
#              It also prints the average of the generated numbers, and the maximum and
#              minimum values. 

import random # To generate random numbers

# Welcome Banner
print("Welcome to the Random Number Generator.\n")

# Initialize variables
asking  = True # Sentinal variable to continue the loop

# Ask the user for the number of random numbers to generate.
while asking:
    try:
        count = int(input("How many numbers would you like to generate?: "))
    except ValueError:
        # Received bad input, provide message and loop again.
        print("\nThat was not a valid input. Please enter valid integers.")
        continue

    try:
        low = int(input("What is the lowest possible value?: "))
    except ValueError:
        # Received bad input, provide message and loop again.
        print("\nThat was not a valid input. Please enter valid integers.")
        continue

    try:
        high = int(input("What is the highest possible value?: "))
    except ValueError:
        # Received bad input, provide message and loop again.
        print("\nThat was not a valid input. Please enter valid integers.")
        continue

    if (low >= high):
        print("\nLowest number must be less than the highest number. Please try again.")
        continue
    else:
        asking = True # All inputs are valid, so we can continue.

    # Generate the random numbers.
    numbers = [random.randrange(low, high+1) for _ in range(count)]
    print(f"\nGenerating numbers:", *numbers) # Prints the numbers in a single line outside of list format.

    # Determine the average, maximum, and minimum values.
    average = sum(numbers) / count
    minimum = min(numbers)
    maximum = max(numbers)

    # Print the results.
    print(f"The lowest number is: {minimum}") 
    print(f"The highest number is: {maximum}")
    print(f"The average is: {average:.2f}")

    # Ask the user if they want to run the program again.
    run_again = input("Would you like to run the program again? (y/n): ").lower()
    if run_again != "y":
        asking = False
        print("Thank you. Have a great day!")