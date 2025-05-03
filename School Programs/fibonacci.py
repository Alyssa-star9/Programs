# AD-1051350-fibonacci.py
#
# Description: This program asks for a valid integer >= 0 and generates the Fibonacci 
#              sequence up to that number. It uses a while loop to validate the input 
#              and a for loop to generate the Fibonacci sequence. It also prints the factorial
#              of the given index of the fibonacci number using a while loop.

# Sentinel variable to continue the loop
asking  = True

# Get the input and validate it with a while loop.
while asking:
    try:
        num = int(input("Please enter an integer: "))
        if num >= 0:
            asking = False
        else:
            print("Not valid input. Please try again.")
    except:
        print("Not valid input. Please try again.")

# Once given a valid input, we can generate the Fibonacci sequence.
if (num == 0):
    print("Fibonacci sequence: 0")
elif (num == 1):
    print("0, 1")
else:
    first_fib = 0
    sec_fib = 1
    print("0, 1", end="") # Start the line with the first two numbers

    i = 2 # Start the loop at 2 since we already printed the first two numbers
    while (i <= num):
        next_fib = first_fib + sec_fib
        print(", ", str(next_fib), end="")
        first_fib = sec_fib
        sec_fib = next_fib
        i += 1
    
# Print the factorial of the given index of the fibonacci number.
factorial = 1  # Initialize factorial variable
i = 1
while i <= num:
    factorial *= i
    i += 1
print(f"\nThe factorial of {num} is: {factorial}")