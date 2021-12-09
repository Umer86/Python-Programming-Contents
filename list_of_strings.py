def list_of_string_func(string_list):
    for planet in string_list:
        if planet == "Sun":
            print(planet, "is not planet.")
        else:
            print(planet, "is planet.")
        if planet == "Mercury":
            print(planet, "is closest to the sun.")


list_of_string_func(['Sun', 'Mercury', 'Venus', 'Earth', 'Mars'])


def iterate_strings(strings):
    print(strings, "is Iterated:\n")
    for x in strings:
        print(x)


iterate_strings('Umer')
