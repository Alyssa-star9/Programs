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
        low = int(input("What is the lowest possible value?: "))
        high = int(input("What is the highest possible value?: "))
        
        # Received bad input, provide message and loop again.
        if (count <= 0):
            print("\nThis program can only generate 1 or more numbers. Try again.")
            continue
        elif (low >= high):
            print("\nLowest number must be less than the highest number. Please try again.")
            continue
    except:
        print("\nThat was not a valid input. Please enter valid integers.")
        continue
    
    # Generate the random numbers.
    print("\nGenerated numbers: ", end="")

    # Determine the first random number and initialize variables.
    total = 0
    first_number = random.randint(low, high)
    print(first_number, end=" ")
    total += first_number
    min_num = first_number
    max_num = first_number

    # Generate the rest of the random numbers.
    for i in range(1, count):
        numbers = random.randint(low, high) 
        print(numbers, end=" ")
        total = total + numbers
        
        # Determine the minimum and maximum values.
        if (numbers < min_num):
            min_num = numbers
        elif (numbers > max_num):
            max_num = numbers

    # Calculate the average.
    average = total /count

    # Print the results.
    print(f"\nThe lowest number is: {min_num}") 
    print(f"The highest number is: {max_num}")
    print(f"The average is: {average:.2f}")

    # Ask the user if they want to run the program again.
    play_again = input("\nPlay again? (y/n): ")
    if play_again != "y":
        asking = False
        print("\nThank you. Have a great day!")