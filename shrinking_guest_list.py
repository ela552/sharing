guest_list = ["merkel", "oprah", "kay"]
guest_list[2] = "rice"
print(guest_list)

print("\nDear guests,")
print("\tBecause we have been able to find a bigger table, we shall invite three more guests.")

guest_list.insert(0, "meghan")
guest_list.insert(2, "kris")
guest_list.append("beyonce")

print(guest_list)

print("\nDear guests,")
print("\tThe bigger table we had hoped to have will not arrive on time, so we shall only be able to invite two guests.")

popped_guest = guest_list.pop()
print(guest_list)
print(
    "\nDear," + " " + popped_guest.title() + " " + "you have been un-invited to the dinner" + "." + "my sincere "
                                                                                                    "apologies.")

popped_guest = guest_list.pop()
print(guest_list)
print(
    "\nDear," + " " + popped_guest.title() + " " + "you have been un-invited to the dinner" + "." + "my sincere "
                                                                                                    "apologies.")
popped_guest = guest_list.pop()
print(guest_list)
print(
    "\nDear," + " " + popped_guest.title() + " " + "you have been un-invited to the dinner" + "." + "my sincere "
                                                                                                    "apologies.")
popped_guest = guest_list.pop()
print(guest_list)
print(
    "\nDear," + " " + popped_guest.title() + " " + "you have been un-invited to the dinner" + "." + "my sincere "
                                                                                                    "apologies.")

print("\nDear," + " " + guest_list[0].title() + " " + "you have are still invited to the dinner" + ".")
print("\nDear," + " " + guest_list[1].title() + " " + "you have are still invited to the dinner" + ".")

print(guest_list)

del guest_list[0]

print(guest_list)

del guest_list[0]
print(guest_list)
