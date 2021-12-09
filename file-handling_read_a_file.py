def read_file_function(file):
    """This function helps to read the file."""
    f = open(file, mode='r')
    print('Type of File:', type(f))
    count = 0
    line = f.readline()

    while line:
        print("\n", line, end="")
        # Get the next line in the file
        line = f.readline()
        count += 1
    print('\n')
    print('The total number of lines are: {}'.format(count))
    f.close()


def read_reverse_append(file1, file2):
    """ This function helps to read the file, reverse the content of the file and in the last append that
    reversed-content other file or write to other file. """
    with open(file1, 'r') as f1:
        lst = f1.readlines()
        # Reverse
        lst.reverse()

        # Append
        f2 = open(file2, mode='a')
        f2.writelines(lst)
        f2.close()


def read_append_to_same_file(file):
    """This function helps to read and write to the same file."""
    file_same = open(file, mode='r+')

    # Read the content
    line = file_same.readlines()
    # Append new text to the same file.
    print("After Inserting/Writing new lines to the same file.\n")

    line.append('This new line1.')
    line.append('This new line2.')
    line.append('This new line3.')

    file_same.writelines(line)
    file_same.close()


def read_write_to_new_file(file1, file2):
    """ This function read the file and write the content of that file to the new file."""
    with open(file1, mode='r') as file:
        text = file.read()

        # Write the Text to new file
        fin = open(file2, mode='w')

        # Write
        fin.writelines(text)
        fin.close()


def main():
    # Print the type of the stream f
    read_file_function('file_handling_file.txt')

    print('\n')
    read_reverse_append('file_handling_file.txt', 'new_file_after_append')

    read_append_to_same_file("same_file.txt")
    read_write_to_new_file("file_handling_file.txt", "file_handling_COPY.txt")


if __name__ == "__main__":
    main()
