sandwich_orders = ["chicken sandwich", "pastrami sandwich", "beef sandwich", "vegetable sandwich",
                   "pastrami sandwich", "tuna sandwich", "pastrami sandwich"]

print("The Deli has run out of pastrami sandwich!")
print("\nAvailable are the following sandwiches:")

while "pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("pastrami sandwich")
for sandwich_order in sandwich_orders:
    print(sandwich_order.title())