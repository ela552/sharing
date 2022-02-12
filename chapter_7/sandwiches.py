sandwich_orders = ["chicken sandwich", "beef sandwich", "vegetable sandwich", "tuna sandwich"]
finished_sandwiches =[]

while sandwich_orders:
    in_process_order = sandwich_orders.pop()

    print("we are currently preparing a;" + in_process_order.title())
    finished_sandwiches.append(in_process_order)

print("\nThe following sandwich is ready: ")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())
