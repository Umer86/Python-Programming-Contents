def iterate_name_func(name_String):
    letter_count = 0
    print(name_String, "is spelled as:")
    for x in name_String:
        print(x, end=' ')
        letter_count += 1
    print("")
    print(letter_count, "letters in the name", name_String)


iterate_name_func("Umer Farooq")
