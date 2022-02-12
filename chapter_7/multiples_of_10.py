# using the input function to determine whether a number entered is a multiple of 10

number = input("Enter a number: ")
number = int(number)
if number % 10 == 0:
    print("This is a multiple of ten!")
else:
    print("This is not a multiple of ten!")
