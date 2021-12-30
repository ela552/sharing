guest_list = ["merkel", "oprah", "kay"]
guest_list[2] = "rice"
print(guest_list)

print("Dear guests,")
print("Because we have been able to find a bigger table, we shall invite three more guests.")

guest_list.insert(0, "meghan")
guest_list.insert(2, "kris")
guest_list.append("beyonce")

print(guest_list)
print("Hello" + " " + guest_list[0].title() + "," + "you are invited to dinner this evening at my residence" + ".")
print("Hello" + " " + guest_list[1].title() + "," + "you are invited to dinner this evening at my residence" + ".")
print("Hello" + " " + guest_list[2].title() + "," + "you are invited to dinner this evening at my residence" + ".")
print("Hello" + " " + guest_list[3].title() + "," + "you are invited to dinner this evening at my residence" + ".")
print("Hello" + " " + guest_list[4].title() + "," + "you are invited to dinner this evening at my residence" + ".")
print("Hello" + " " + guest_list[5].title() + "," + "you are invited to dinner this evening at my residence" + ".")

