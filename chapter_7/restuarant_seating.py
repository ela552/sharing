# A program asking how many people are in a dinner group using the input function

dinner_group = input("what the group number? ")
dinner_group = int(dinner_group)
if dinner_group > 8:
    print("You will have to wait for a table,sorry for the inconvenience!")
else:
    print("Your table is ready!")
