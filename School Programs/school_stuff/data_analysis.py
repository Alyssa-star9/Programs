# last practice run through

# getting the initial values function
def get_marks():
    """Gets the input from the user until -1 is entered and returns a list
    of the entered marks.
    Args: none
    Returns: list called marks
    """
    num = 0 # initialize
    marks = []
    while (num != -1):
        try:
            num = int(input("Enter a number b/w 0 and 10 (enter '-1' to stop): "))
            
            if (num == -1):
                break
            elif (num < 1) or (num > 10):
                print("Invalid input. Please enter an integer b/w 0 and 10.\n")
            else:
                marks.append(num) # to get the list
            
        except:
            print("Invalid input. Please enter an integer b/w 0 and 10.\n")
    
    print(f"\nThe list of numbers is: {marks}")
    return marks

# mean function
def mean(marks):
    """Returns the arithmetic mean of the marks.
    Args: marks; a list
    Returns: an integer
    """
    avg = sum(marks) / len(marks)
    
    return avg


# median function
def median(marks):
    """Returns the median of the marks.
    Args: marks; a list
    Returns: an integer
    """
    if (len(marks) % 2 != 0):
        ind = (len(marks) - 1) // 2
        med = marks[ind]
    else:
        mid_ind1 = (len(marks) // 2) - 1
        mid_ind2 = len(marks) // 2
        med = (marks[mid_ind1] + marks[mid_ind2]) / 2
        
    return med

# frequency function    
def freq(marks):
    """Determines and prints a list of the frequency of each number.
    Args: a list; marks
    Returns: a list called freq_list that contains the frequency of each mark
    """
    freq_list = [0] * 11 # create a list with 11 zeroes (indices 0 to 10)
    for mark in marks:
        if (mark >= 0) and (mark <= 10):
            freq_list[mark] += 1
    
    return freq_list

# mode function
def mode(freq_list):
    """Determines the option that repeats the most often.
    Args: freq_list; a list from 
    Returns: a list called mode_list that contains the mode of the marks
    """
    mode_list = []
    max_freq = max(freq_list)
    
    for num in range(len(freq_list)):
        if (freq_list[num] == max_freq) and (max_freq > 0):
            mode_list.append(num)
    
    return mode_list

# menu function to run program
def menu():
    """Main function for program to run
    Args: none
    Returns: choice; an integer from 
    """
    print("\n1 = mean")
    print("2 = median")
    print("3 = frequency")
    print("4 = mode")
    
    choice = int(input("Enter a choice from 1-4 (enter 5 to quit program): "))
    if (choice == 5):
        print("\nThanks for playing!")
    return choice


# main program
marks = get_marks()
choice = menu()
freq_list = freq(marks)

while (choice != 5):
    if (choice == 1):
        print(f"The average is: {mean(marks)}")
    elif (choice == 2):
        print(f"The median is: {median(marks)}")
    elif (choice == 3):
        print(f"The frequency is: {freq(marks)}")
    elif (choice == 4):
        print(f"The mode is {mode(freq_list)}")
        
    choice = menu() 