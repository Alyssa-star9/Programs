# File Name: AD-1051350-standard_dev.py
# Description: This receives a certain number of values and returns the standard deviation.
#              It also prints the numbers in a list, as well as the mean and standard deviation.
#              The goal is to use custom functions and practice formatting.

# Import the math module to use the sqrt function.
import math

# Create a function to calculate the mean.
def mean():
    """This function calculates the mean of the data list
    Args: none 
    Returns: mean as a float
    """
    total = 0
    for num in data:
        total += num
        mean = total / len(data)
    return mean

# Create a function to calculate the standard deviation.
def stand_dev():
    """This function calculates the standard deviation of the data list
    Args: none
    Returns: standard deviation as a float
    """
    mean_value = mean()
    total = 0
    for num in data:
        total += (num - mean_value) ** 2
    res = total / len(data)
    dev = math.sqrt(res)
    return dev

# Welcome Banner
print("Welcome to the Standard Deviation Calculator!\n")

# Get the inputs from the user to begin the program.
asking = True
while asking:
    try:
        num_data = int(input("How many pieces of data?: "))
        if (num_data <= 1):
            print("Please enter an integer >1.")
        else:
            asking = False

    except:
        print("Please enter an integer >1.")

# Create a list to store the numbers.
trying = True
while trying:
    try:
        data = []
        for i in range(num_data):
            valid_input = False
            while not valid_input:
                try:
                    count = float(input(f"# {i + 1}: "))
                    data.append(count)
                    valid_input = True
                except:
                    print("Enter valid numbers only.")
        print(f"data: {data}")
        trying = False
    except:
        print("Enter valid numbers only.")

# Print the mean and standard deviation.
print(f"mean: {mean()}")
print(f"standard variation: {stand_dev()}")