# Enter an integer and check if the value is isnumeric?

x = input("Input a number: ")

# Since we want integers, so convert it into int
print(type(x))
try:
    if x.isnumeric():
        number = int(x)
        if number >= 1:
            print("Your number {} is positive and isnumeric!!!".format(number))
        if number == 0:
            print("Your number {} is Zero and isnumeric!!!".format(number))
    else:
        raise ValueError
except ValueError as e:
    print("Your entered value is not Numeric and isnumeric support only positive numeric values")
    print(e)
