def import_and_create_dict(file):
    """ This function is used to create an expense dictionary from a file. Every line in the file should be in the
    format, key, value. The key is a user's name and the value is an expense to update the user's total expense with.
    The value should be a number, however, it is possible that there is no value, that the value is an invalid
    number, or that the entire line is blank.
    """
    with open(file, mode='r') as f:

        lines = f.readlines()
        expenses = {}
        for line in lines:
            # Remove whitespaces and split into list.
            lst = line.strip().split(",")
            # removing any missing values:
            if len(lst) <= 1:
                continue
            key = lst[0].strip()
            value = lst[1].strip()

            try:
                value = float(value)

                expenses[key] = expenses.get(key, 0) + value
            except:
                continue

        return expenses


def main():
    expenses_list = import_and_create_dict("expenses.txt")
    print("List of Expenses: {}".format(expenses_list))


if __name__ == "__main__":
    main()
