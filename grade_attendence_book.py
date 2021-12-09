umer = {
    'name': 'Umer Farooq',
    'grades': [80, 90, 45, 80, 100],
    'attendence': [True, True, False, True, True]
}

ramsha = {
    'name': 'Ramsha',
    'grades': [80, 90, 100, 80, 100],
    'attendence': [True, False, True, True, True]
}

xyz = {
    'name': 'Xyz',
    'grades': [0, 90, 0, 80, 0],
    'attendence': [True, False, False, False, True]
}

student_dict = {'1': umer, '2': ramsha, '3': xyz}
# Print the keys of Dict_student
print(student_dict.keys())
# Print key along with values

for k, v in student_dict.items():
    print('Key:', k, "Values:", v)

# get Umer attendence
umer_attend = student_dict['1']
print('Umer Attendence:', umer['attendence'])

# Get Ramsha all records

ramsha_records = student_dict['2']
records = ramsha_records.items()
print('Ramsha Details are:\n')

for k, v in records:
    print(k, v)

# First way: get avg of students grades

avg_mrks = student_dict.items()

average_grade = []

for key, val in avg_mrks:
    for i in val["grades"]:
        # print('\n',i)
        average_grade.append(i)

print("\n", round(sum(average_grade) / len(average_grade)))


# Second way: get avg of students grades

items = student_dict.items()

con_average_grade = []

for key, val in items:
    con_average_grade += val['grades']

print("\n", round(sum(con_average_grade) / len(con_average_grade)))
