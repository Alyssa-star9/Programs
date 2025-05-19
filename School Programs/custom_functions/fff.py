# File Name: AD-1051350-fff.py
# Description: "Fibonacci Function Functions"
#              This programs receives a valid integer and indicates the fibonacci sequence
#              up to that index number. It then determines the facotrial of each number
#              in the sequence. The results are then printed.

# Custom function to get an integer index for the Fibonacci sequence.
def get_int():
    """This function gets a valid integer input from the user.
    Args: none
    Returns: an integer >= 0
    """
    asking = True # sentinel variable
    while asking:
        try:
            ind = int(input("Enter an index >= 0: "))

            if (ind < 0):
                print("Invalid input. Please enter a number >= 0.")
            elif (ind == 0):
                print("F Sequence to index 0 is: 0")
                print("F Factorial to index 0 is: 1")
                return 0 # will directly return 0 and exit the loop
            else:
                asking = False
        except:
            print("Invalid input. Please enter a number >= 0.")
    return ind

# Custom function to determine the Fibonacci sequence up to the given index.
def fib_seq(ind):
    """This function determines and prints the Fibonacci sequence up to the given index.
    Args: a valid integer >= 0 reopresetning an index
    Returns: a list of Fibonacci numbers up to the provided input integer
    """
    fib = [0, 1] # Initialize the Fibonacci sequence with the first two numbers
    for i in range(2, ind + 1):
        fib.append(fib[i - 1] + fib[i - 2]) # Calculate the next Fibonacci number
    return fib[:ind + 1] # Slice in case ind < 2
    
# Custom function to determine the factorial of each number in the printed Fibonacci sequence.
def fact(n):
    """This function determines the factorial of each number in the Fibonacci sequence.
    Args: a valid integer >= 0:
    Returns: the factorial of the provided input integer
    """
    if (n == 0) or (n == 1):
        return 1
    else:
        return n * fact(n - 1)


# Custom function to get the main program to run.
def main():
    index = get_int()
    if index > 0:
        fib_nums = fib_seq(index)
        fact_nums = [fact(num) for num in fib_nums]
        print(f"F Sequence to index {index} is:\t", " ".join(str(num) for num in fib_nums))
        print(f"F Factorial to index {index} is:\t", " ".join(str(fact) for fact in fact_nums))

# Run the program
main()