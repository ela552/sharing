# Use a break statement to exit the loop when the user enters a 'quit' value.

prompt = "\nPlease enter your age: "
prompt += "\nEnter 'quit' when done."

active = True
while active:
    age = input(prompt)

    if age == 'quit':
        break
    else:
        print(age)