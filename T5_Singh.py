# program to calculate the average of all the numbers from the file you created (Tnumbers.txt)


class ReadFile:

    # reads a file at given path, read the content and calculate average

    def read_file(self):
        f = open("Tnumbers.txt", "r")
        sum = 0
        count = 0
        line = f.readline().strip()
        while line != "":
            try:
                sum += int(line)
                print(line)
                count = count + 1
            except:
                sum += 0
            line = f.readline().strip()

        f.close()
        avg = round(sum/count,3)
        # store the result in results.txt file
        f1 = open("results.txt", "w")
        f1.write(str(avg))
        f1.close()



# this class is used to run stdio for this program

class RunInput:
    # constructor function
    def __init__(self):
        reader = ReadFile()
        reader.read_file()


run = RunInput()

