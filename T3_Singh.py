
# program to calculate the monthly and annual expense to maintain a car by a user
import locale


# class that maintains the monthly expense breakdown and calculates the monthly and annual expense
class ExpenseCal:
    loan = 0
    insurance = 0
    gas = 0
    oil = 0
    tires = 0
    maintenance = 0
    monthly_expense = 0
    annual_expense = 0
    locale.setlocale(locale.LC_ALL, '')

    # constructor function
    def __init__(self, l, i, g, o, t, m):
        self.loan = l
        self.insurance = i
        self.gas = g
        self.oil = o
        self.tires = t
        self.maintenance = m

    # calculating the monthly and annual expense
    def cal_expense(self):
        self.monthly_expense = self.loan + self.insurance + self.gas + self.oil + self.tires + self.maintenance
        self.annual_expense = self.monthly_expense * 12
        self.print_expense()

    # display the monthly and annual expense
    def print_expense(self):
        print("Total monthly expense:", locale.currency(self.monthly_expense, grouping=True))
        print("Total annual expense:", locale.currency(self.annual_expense, grouping=True))


# this class is used to run stdio for this program
class RunInput:
    # constructor function
    def __init__(self):
        while True:
            # ask user to input the actual value of property in dollars
            try:
                l = float(input("Enter the monthly loan amount: ").strip())
                i = float(input("Enter the monthly insurance amount: ").strip())
                g = float(input("Enter the monthly gas amount: ").strip())
                o = float(input("Enter the monthly oil amount: ").strip())
                t = float(input("Enter the monthly tires amount: ").strip())
                m = float(input("Enter the monthly maintenance amount: ").strip())
                exp = ExpenseCal(l, i, g, o, t, m)
                exp.cal_expense()
            except ValueError:
                print("Invalid value provided. Try again...")
            except:
                print("please try again....")


run = RunInput()




