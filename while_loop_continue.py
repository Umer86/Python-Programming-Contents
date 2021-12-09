for x in range(1, 30):
    # Find Odd numbers:
    if x % 2 != 0:
        if x % 3 == 0:
            continue
        print(x)
