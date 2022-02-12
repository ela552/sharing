# Add code near the beginning of your program to print a message saying the deli has run out of pastrami
# then use a while loop to remove all occurrences of 'pastrami' from sandwich_orders.
# Make sure no pastrami sandwiches end up in finished_sandwiches.

sandwich_orders = ["chicken sandwich", "pastrami sandwich", "beef sandwich", "vegetable sandwich",
                   "pastrami sandwich", "tuna sandwich", "pastrami sandwich"]
finished_sandwiches =[]

print("The Deli has run out of pastrami sandwich!")

while "pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("pastrami sandwich")
while sandwich_orders:
    in_process_order = sandwich_orders.pop()

    print("we are currently preparing a;" + in_process_order.title())
    finished_sandwiches.append(in_process_order)

print("\nThe following sandwich is ready: ")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())