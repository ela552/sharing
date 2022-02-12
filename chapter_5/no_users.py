usernames = []
if usernames:
    for username in usernames:
        if username == "admin":
            print("Hello" + " " + username + "," + " " + "would you like to see a status report?")
        else:
            print("hello" + " " + username + "," + " " + "thank you for logging in again.")
else:
    print("we need to find some users! ")

