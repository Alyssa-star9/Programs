#Practice for 2D Collections and Lists.
#This program will create a number pad similar to the ones you will see on a phone.
#Note that this can be done using lists, sets, or tuples.

#Create the number pad.
num_pad = ((1, 2, 3),
           (4, 5, 6),
           (7, 8, 9),
           ("*", 0, "#")) #Note that writing each tuple of seperate lines is not required, but is just easier to read.

#Print the number pad.
for row in num_pad:
    for num in row:
        print(num, end=" ")
    print()