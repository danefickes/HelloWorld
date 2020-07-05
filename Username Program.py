username = input("What would you like your username to be? ")
username_charaters = len(username)
if username_charaters < 3:
    print("name must be at least 3 characters")
elif username_charaters > 50:
    print('name can be a maximum of 50 character')
else:
    print(f"Welcome {username}.")