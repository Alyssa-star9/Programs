import random

#Set default values.
width = 8
low = 1
high = 100 

#Get the number of numbers.
loop = int(input("How many numbers?: "))

#Print the banner.
print(f"Your {loop} random numbers are:\n") 
    
#Determine the frequency.
r20 = 0
r40 = 0
r60 = 0
r80 = 0
r100 = 0

for i in range(1, loop + 1):
    num = random.randint(low, high)
    if (num >= 1) and (num <= 20):
        r20 += 1
    elif (num >= 21) and (num <= 40):
        r40 += 1
    elif (num >= 41) and (num <= 60):
        r60 += 1
    elif (num >= 61) and (num <= 80):
        r80 += 1
    else:
        r100 += 1
        
#Print the result.
    print(str(num) + "\t", end =" ")
    
#Make condition for new line.
    if (i % width == 0):
        print()

#Print the frequency and output sequence.
print()
print("-" * 50)
print("The frequency of each range is:\n")
print("1 - 20: " + ("*" * r20) + " (" + str(r20) + ")")
print("21 - 40: " + ("*" * r40) + " (" + str(r40) + ")")
print("41 - 60: " + ("*" * r60) + " (" + str(r60) + ")")
print("61 - 80: " + ("*" * r80) + " (" + str(r80) + ")")
print("81 - 100: " + ("*" * r100) + " (" + str(r100) + ")")
