# program to display file content


class ReadFile:

    # reads a file at given path, prints the content and closes the file object to avoid memory leak
    def read_file(self, filepath):
        f = open(filepath, "r")
        s = f.read()
        print(s)
        f.close()


# this class is used to run stdio for this program
class RunInput:
    # constructor function
    def __init__(self):
        reader = ReadFile()
        reader.read_file("numbers.txt")


run = RunInput()

