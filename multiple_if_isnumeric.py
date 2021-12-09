# Ask for User input
x = input("Enter the number:  ")

# Check wether the input number is int or str
print(type(x))
number = int(x)
# isnumeric only works with positive integers
if x.isnumeric():
    if number >= 1:
        print("Your number {} is positive!!!".format(number))
    if number == 0:
        print("Your number {} is Zero!!!".format(number))
else:
    print("Your number {} is Negative!!!".format(number))
