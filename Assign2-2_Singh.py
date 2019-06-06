# This assignment asks to write a program in which
# total travel distance is calculated using a loop structure.


class DistanceTraveled:
    speed = 0  # speed is in miles per hours
    time = 0  # time is in hour
    distance = 0  # distance is in miles

    # constructor function
    def __init__(self, speed, time):
        self.speed = speed
        self.time = time

    # calculate distance in loop structure
    def calculate_distance(self):
        print('Hour', 'Distance Traveled')
        print('--------------------------')
        t1 = int(self.time)
        t2 = self.time - t1
        i = 0
        for i in range(t1):
            self.distance += self.speed
            print(i+1, "   ", round(self.distance, 2))
        if t2 > 0:
            self.distance += self.speed * t2
            print(i+2, "   ", round(self.distance, 2))


# this class is used to run stdio for this program
class RunInput:
    # constructor function
    def __init__(self):
        while True:
            try:
                speed = float(input("Enter the speed of the vehicle in mph ").strip())
                time = float(input("Enter the number of hours traveled ").strip())
                distance_mph = DistanceTraveled(speed, time)
                distance_mph.calculate_distance()
            except ValueError:
                print("Invalid value provided. Try again...")
            except:
                print("please try again....")

# initiating the script from here
vechiledistance = RunInput()

