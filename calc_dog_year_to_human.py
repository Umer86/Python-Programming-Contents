"""import traceback

def calculator():
    # Get dog age
    age = input("Input dog years: ")
    try:
        d_age = float(age)
        dog_age_in_human_age=0
        if d_age==0:
            print(age, "is an invalid age.")
            exit()
        elif d_age==1:
            dog_age_in_human_age =d_age*15
        elif 1<d_age<=2:
            dog_age_in_human_age =d_age*12
        elif 2<d_age<=3:
            dog_age_in_human_age =d_age*9.3
        elif 3<d_age<=4:
            dog_age_in_human_age =d_age*8
        elif 4<d_age<=5:
            dog_age_in_human_age =d_age*7.2
        else:
            dog_age_in_human_age =5*7.2 + (d_age-5)* 7
    except ValueError as e:
        print(traceback.format_exc(e))

    if flag==False:
        print("The given dog age {} is {} in human years".format(d_age, round(dog_age_in_human_age, 2)))
    else:
        print("Age cannot be a negative number.")


calculator() # This line calls the calculator function"""

import traceback


def calculator():
    age = input("Input dog years: ")
    try:
        d_age = float(age)
        dog_age_in_human_age = 0
        if d_age < 0:
            print("Age cannot be a negative number.")
            exit()
        if d_age == 0:
            raise ValueError
        elif d_age == 1:
            dog_age_in_human_age = 15
        elif 1 < d_age <= 2:
            dog_age_in_human_age = d_age * 12
        elif 2 < d_age <= 3:
            dog_age_in_human_age = d_age * 9.3
        elif 3 < d_age <= 4:
            dog_age_in_human_age = d_age * 8
        elif 4 < d_age <= 5:
            dog_age_in_human_age = d_age * 7.2
        else:
            dog_age_in_human_age = 5 * 7.2 + (d_age - 5) * 7

        print("The given dog age {} is {} in human years".format(d_age, round(dog_age_in_human_age, 2)))
    except ValueError as e:
        print(age, "is an invalid age.")
        print(traceback.format_exc())


calculator()  # This line calls the calculator function
