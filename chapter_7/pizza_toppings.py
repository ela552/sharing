# using while and the input function
prompt = "\nEnter a desired pizza topping: "
prompt += "\nEnter 'quit' when done!"

pizza_topping = " "
while pizza_topping != 'quit':
    pizza_topping =input(prompt)
    if pizza_topping != 'quit':
        print("\n")
        print(pizza_topping.title() + " " + "will be added to your pizza!")

