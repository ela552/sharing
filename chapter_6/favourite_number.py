favourite_numbers = {"stellah": [13, 4, 8, 20],
                     "paul": [8, 2, 3],
                     "david": [13, 24],
                     "juliet": [11],
                     "mart": [4, 0, 64, 73, 89],
                     }

for name, numbers in favourite_numbers.items():
    print("\n" + name.title() + "'s" + " " + "favourite numbers are:")
    for number in numbers:
        print("\t" + str(number))
