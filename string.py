# Double the given string and then add length of that doubled word.

def double_word(word):
    result = word * 2
    length_word = len(result)
    return result + str(length_word)


print(double_word("Hello"))
print(double_word("IT"))
print(double_word("Umer"))
print(double_word(" "))
