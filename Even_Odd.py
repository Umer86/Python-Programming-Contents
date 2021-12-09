# This program will help you to identity if the required number is Even or Odd

# Write Function that returns the required Even or Odd result.

def even_or_odd(number):
    results = True
    if number % 2 == 0:
        print("The Number {} is even".format(number), end="!!!")

    if number % 2 != 0:
        print("The Number {} is odd".format(number), end="!!!")


num = int(input("Enter the number:  "))
even_or_odd(num)
