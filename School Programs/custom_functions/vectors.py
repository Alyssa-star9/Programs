# File Name: AD-1051350-vectors.py
# Description: This program receives two lists of three numbers, each representing a vector in 3D space.
#              It calculates the sum, difference, dot product, and cross product of the two vectors.
#              The results are then printed.

# Custom function for vector addition
def vec_add(A, B):
    """This function adds two vectors A and B.
    Args: A, B: lists of three numbers each
    Returns: A + B as a list
    """
    return [A[0] + B[0], A[1] + B[1], A[2] + B[2]]

# Custom function for vector subtraction
def vec_sub(A, B):
    """This function subtracts two vectors A and B.
    Args: A, B: lists of three numbers each
    Returns: A - B as a list
    """
    return [A[0] - B[0], A[1] - B[1], A[2] - B[2]]

# Custom function for dot product (scalar multiplication)
def dot_product(A, B):
    """This function calculates the product of two vectors A and B.
    Args: A, B: lists of three numbers each
    Retruns: A * B as a float
    """
    return (A[0] * B[0]) + (A[1] * B[1]) + (A[2] * B[2])

# Custom function for cross product (cross product)
def cross_product(A, B):
    """This function calculates the cross product of two vectors A and B.
    Args: A, B: lists of three numbers each
    Returns: A x B as a list
    """
    return [(A[1] * B[2]) - (A[2] * B[1]),
            (A[2] * B[0]) - (A[0] * B[2]),
            (A[0] * B[1]) - (A[1] * B[0])]

# Instructions
print("Enter components of two vectors A and B, seperated by spaces.\n")

asking = True # sentinel variable
while asking:
    try:
       # Make the values of A and B into lists
       A = []
       B = []
       for i in input("Enter A; x1 y1 z1: ").split():
            A.append(float(i))
       for i in input("Enter B; x2 y2 z2: ").split():
            B.append(float(i))

        # Check if the input is valid
       if (len(A) != 3) or (len(B) != 3):
            print("Try again. Please enter 3 items for each A, B")
       else:
            asking = False
    except:
        print("Invalid input. Please enter numbers.")

# Print the addition, subtraction, dot product, and cross product of the vectors.
# A for loop will be used to print the results.
