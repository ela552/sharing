# Write a program that polls users about their dream vacation.
# Write a prompt similar to If you could visit one place in the world,
# where would you go? Include a block of code that prints the results of the poll.

responses = {}

polling_active = True

while polling_active:
    name = input("what is your name?")
    response = input("If you could visit ay place in the world, where would you go?")

    responses[name] = response

    repeat = input("would you like to let another person answer? ('yes'/'no') ")
    if repeat == 'no':
        polling_active = False

print("....Polling Results....")
for name, response in responses.items():
    print(name + "'s" + " " + "dream destination is" + " " + response)