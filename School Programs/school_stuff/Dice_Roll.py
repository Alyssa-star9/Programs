#Random module will be used to generate random quantities of rolls.
import random

#Welcome Banner
print("Welcome to the Dice Roll Tracker")

#Prompt the user to imput the number of rolls.
num_rolls = int(input("\nHow many rolls?: "))

#Determine the number of rolls.
r1 = 0
r2 = 0
r3 = 0
r4 = 0
r5 = 0
r6 = 0
for i in range(0, num_rolls):
    r = random.randint(1, 6)
    if (r == 1):
        r1 += 1
    elif (r == 2):
        r2 += 1
    elif (r == 3):
        r3 += 1
    elif (r == 4):
        r4 += 1
    elif (r == 5):
        r5 += 1
    elif (r == 6):
        r6 += 1

#Percent of each roll.
perc_1 = (r1 / num_rolls) * 100
perc_2 = (r2 / num_rolls) * 100
perc_3 = (r3 / num_rolls) * 100
perc_4 = (r4 / num_rolls) * 100
perc_5 = (r5 / num_rolls) * 100
perc_6 = (r6 / num_rolls) * 100

#Print the results.
print("1 was rolled: " + str(r1) + " times, or " + str(round(perc_1, 2)) + "%")
print("2 was rolled: " + str(r2) + " times, or " + str(round(perc_2, 2)) + "%")
print("3 was rolled: " + str(r3) + " times, or " + str(round(perc_3, 2)) + "%")
print("4 was rolled: " + str(r4) + " times, or " + str(round(perc_4, 2)) + "%")
print("5 was rolled: " + str(r5) + " times, or " + str(round(perc_5, 2)) + "%")
print("6 was rolled: " + str(r6) + " times, or " + str(round(perc_6, 2)) + "%")