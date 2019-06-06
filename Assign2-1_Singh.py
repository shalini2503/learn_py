# This assignment asks to write a program that calculates
# and displays a person's body mass index (BM)


class Assign2:

    height = 0  # height is in inches
    weight = 0  # weight is in pounds
    msg = ""

    # constructor function
    def __init__(self, h, w):
        self.height = h
        self.weight = w

    # formula to calculate BMI
    def calculate_bmi(self):
        bmi = self.weight*(703/(self.height*self.height))
        # def the body weight based on the BMI value
        if 18.5 < bmi < 25:
            self.msg = "Your weight is optimal"
        elif bmi <= 18.5:
            self.msg = "Your weight is underweight"
        else:
            self.msg = "Your weight is overweight"
        return bmi


# this class is used to run stdio for this program
class RunAssign2:

    # constructor function
    def __init__(self):
        while True:
            try:
                ht = float(input("Enter your height in inches ").strip())
                wt = float(input("Enter your weight in pounds ").strip())
                body_index = Assign2(ht, wt)
                print("Your Body Mass Index is", round(body_index.calculate_bmi(), 2))
                print(body_index.msg)
            except ValueError:
                print("Invalid value provided. Try again...")
            except:
                print("please try again....")


# initiating the script from here
runAssign = RunAssign2()

