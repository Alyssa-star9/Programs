#Shopping cart program for practice with while loops, lists, sets, and tuples.

foods = []
prices = []
total = 0

#Determine the items in the shopping cart and the prices.
while True:
    food = input("Enter a food to buy (q to quit): ")
    if (food.lower() == "q"): #The .lower function is used just in case the user inputs "Q" instead of "q".
        break
    else:
        price = float(input(f"Enter the price of a {food}: $"))
        foods.append(food)
        prices.append(price)

#Banner for shopping cart.
print("\n" + "-"*5, "YOUR CART", "-"*5)

#Print the cart.
for food in foods:
    print(food, end=" ")

#Determine the total cost.
for price in prices:
    total += price

#Print the total.
print(f"Your total is: ${total}")

