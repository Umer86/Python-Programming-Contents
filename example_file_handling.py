def function_(file):

    lst = []
    with open(file, mode='r') as file:
        lines = file.readlines()
        for i in range(2):
            lst.append(lines[i].rstrip())
    return lst


print(function_("text.txt"))


