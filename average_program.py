num_list = []  # For storing the entered integers
i = 0  # For counting the entered numbers
loop_termination = True  # It will ask for the numbers

while loop_termination == True:
    num = int(input("Enter the Integer: "))
    # -1 to terminate the program
    if num == -1:
        loop_termination = False
    else:
        num_list.append(num)
        i += 1

# Get the sum of entered numbers: When can do it using len() to find the number entered
num_sum = 0
for x in num_list:
    num_sum += x

# Get the average
num_avg = num_sum / i
print(num_avg)
