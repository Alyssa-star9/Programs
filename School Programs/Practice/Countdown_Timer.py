#This is a countdown timer program using the Time Module.
import time

#Prompt the user to input a time.
my_time = int(input("Enter the time in seconds: "))

#Determine the countdown clock using for loops.
for i in range(my_time, -1, -1):
    seconds = i % 60
    minutes = int(i / 60) % 60
    hours = int(i / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1) #This delays the amount of time it takes for each new time to be displayed.

#Print the countdown.
print("TIME'S UP!")