# Write a loop in which you ask users their age, and then tell them the cost of their movie ticket.

age = input("Please enter your age: ")

age = int(age)
if age < 3:
    print("Your movie ticket is free")
elif age <= 12:
    print("Your movie ticket costs $10")
else:
    print("Your movie ticket costs $20")
