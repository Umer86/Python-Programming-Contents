def numeric_to_letter_grade(num_grade):
    """Conversts the Numbers into Grade."""
    if num_grade >= 90:
        print("A")
    elif num_grade >= 80:
        print("B")
    elif num_grade >= 70:
        print("C")
    elif num_grade >= 50:
        print("C")
    else:
        print("Fail")


x = input("Enter the Number:  ")
number = int(x)

numeric_to_letter_grade(number)

help(numeric_to_letter_grade)
