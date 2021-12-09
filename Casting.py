# Float to Int
# Use int() to cast any datatype to int

a = 400 / 3
print(a)
print(int(a))
print(int("1"))

# Use round() to round any number

a = 400 / 5
print(round(a))

# Print command

print("4 % 2 = ", 4 % 2, end=" ")
print("is Even!!!")

# It will return error, because number and string cannot be concatinated.
# print("4 % 2 = " + 4 % 2)

# So convert the Number into String using str()

print("4 % 2 = " + str(4 % 2))

# Is number is even?
print("Is 4 even?{0}".format(str(4 % 2 == 0)))

