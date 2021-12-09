password = ''

while password != 'Secret':
    password = input("Enter the password:")
    if password == 'Secret':
        print("Welcome!")
    else:
        print("Try Again")
