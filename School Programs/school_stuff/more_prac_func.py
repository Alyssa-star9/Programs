#more ducking practice cuz I gotta do this shi without help

#def every_other(my_list):
#    """Takes a list and returns a list that contains
#    every other element in the list.
#    Args: my_list; essentially the list the user gives.
#    Returns: every other element in the list
#    """ 
#    length = len(my_list)
#    
#    for i in range(0, length, 2):
#        print(my_list[i], end=" ")
#
#
#my_list = []
#num_elem = int(input("Enter the number of elements: "))
#    
#for i in range(num_elem):
#    num = input(f"Enter element {i+1}: ")
#    my_list.append(num)

#every_other(my_list)

#####################################################################
#def bigger_ten(my_list):
#    """Takes a list and returns a list that contains
#    every element >10 in the list.
#    Args: my_list; essentially the list the user gives.
#    Returns: every element >10 in the list
#    """
#    length = len(my_list)
#    
#    for i in range(length):
#        if (my_list[i] > 10):
#            print(my_list[i], end=" ")
#
#my_list = []
#num_elem = int(input("Enter the number of elements: "))
#
#for i in range(num_elem):
#    num = int(input(f"Enter element #{i+1}: "))
#    my_list.append(num)
#    
#bigger_ten(my_list)

#####################################################################
def distance_mean(my_list):
    """Takes a list and returns a list that contains the difference between
    each of the values and the average
    Args: my_list; essentially, valid user input
    Returns: the new list
    """

    
    #calculate the average
    avg = sum(my_list) / len(my_list)
        
    return [num - avg for num in my_list]



my_list = []
num_elem = int(input("Enter the number of elements: "))

for i in range(num_elem):
    num = float(input(f"Enter element #{i+1}: "))
    my_list.append(num)

print(distance_mean(my_list))