# Take user input in numbers
num_grade=input("Enter your Marks: ")

# Cast the input to Integer
num_grade=int(num_grade)

# Testing

if num_grade >=90:
    print("A")
elif num_grade >=80:
    print("B")
elif num_grade >=70:
    print("C")
else:
    print("Fail")
