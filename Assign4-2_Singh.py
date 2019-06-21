# program to print course details using a dictionary


# class to manage Course Details
class CourseDetails:
    rooms = {}
    instructor = {}
    time = {}

    # constructor function
    def __init__(self):
        self.rooms["ISQS 5347"] = "BA 289"
        self.rooms["ISQS 6337"] = "BA 015"
        self.rooms["ISQS 6349"] = "BA 287"
        self.rooms["ISQS 6348"] = "BA 021"

        self.instructor["ISQS 5347"] = "Zadeh"
        self.instructor["ISQS 6337"] = "Song"
        self.instructor["ISQS 6349"] = "Kim"
        self.instructor["ISQS 6348"] = "Benjamin"

        self.time["ISQS 5347"] = "9:00 am"
        self.time["ISQS 6337"] = "2:00 pm"
        self.time["ISQS 6349"] = "9:00 am"
        self.time["ISQS 6348"] = "2:00 pm"

    # prints course details if it exists
    def print_course_details(self, course):
        if course in self.rooms and course in self.instructor and course in self.time :
            print("The details for course " + course + " are: ")
            print("Room: " + self.rooms[course])
            print("Instructor: " + self.instructor[course])
            print("Time: " + self.time[course])
        else:
            print("We do not offer this course")
        print()


# this class is used to run stdio for this program
class RunInput:
    # constructor function
    def __init__(self):

        while True:
            # ask user to input the course name
            details = CourseDetails()
            try:
                details.print_course_details(input("Enter a course number: ").strip())
            except ValueError:
                print("Invalid value provided. Try again...")
            except:
                print("please try again....")


run = RunInput()
