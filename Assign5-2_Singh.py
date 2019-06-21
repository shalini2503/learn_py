# program to display first 5 lines of the file content


class ReadFile:

    # reads a file at given path, prints the content limited to 5 lines at max
    # and closes the file object to avoid memory leak
    def read_file(self, file_path):
        f = open(file_path, "r")
        s = f.read().splitlines()
        i = 0
        for line in s:
            print(line)
            if i == 4:
                break
            else:
                i = i+1

        f.close()


# this class is used to run stdio for this program
class RunInput:
    # constructor function
    def __init__(self):
        reader = ReadFile()
        while True:
            # ask user to input the replacement amount in dollars
            try:
                file_name = input("Enter the name of the file: ").strip()
                reader.read_file(file_name)
            except ValueError:
                print("Invalid value provided. Try again...")
            except:
                print("File not found ....")


run = RunInput()

