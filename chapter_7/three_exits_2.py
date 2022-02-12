# Use an active variable to control how long the loop runs.

prompt = "\nPlease enter your age: "
prompt += "\nEnter 'quit' when done."

active = True
while active:
    age = input(prompt)

    if age == 'quit':
        active = False
    else:
        print(age)
