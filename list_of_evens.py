# In List of numbers, you have to pick the even one only.

def list_of_even(list):
    listofnum = list
    even_list = []
    for i in listofnum:
        if i % 2 == 0:
            even_list.append(i)
            i += 1
    return even_list


print(list_of_even([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15]))
print(list_of_even([18,20,50,60,61]))
