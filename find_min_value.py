def min_function(numbers):
    new_list = []
    min_value = numbers[0]
    for i in numbers:
        if i < min_value:
            min_value = i
            #new_list.append(min_value)
    return min_value


print(min_function([5, 3, 8, -1, -2.2, 0]))
