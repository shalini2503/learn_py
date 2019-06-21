# program to calculate the minimum amount of insurance he or she should buy for the property
import locale


class Insurance:
    replacement_cost = 0
    percent_insured = .80
    minimum_insurance = 0
    locale.setlocale(locale.LC_ALL, '')

    # constructor function
    def __init__(self, cost):
        self.replacement_cost = cost

    # calculating the minimum amount of insurance
    def showInsure(self):
        self.minimum_insurance = self.percent_insured * self.replacement_cost
        # display
        print("Replacement cost:", locale.currency(self.replacement_cost, grouping=True))
        print("Percent insured:", self.percent_insured*100, "%")
        print("Minimum insurance:", locale.currency(self.minimum_insurance, grouping=True))


# this class is used to run stdio for this program
class RunInput:
    # constructor function
    def __init__(self):
        while True:
            # ask user to input the replacement amount in dollars
            try:
                cost = float(input("Enter the replacement amount ").strip())
                cost_of_insurance = Insurance(cost)
                cost_of_insurance.showInsure()
            except ValueError:
                print("Invalid value provided. Try again...")
            except:
                print("please try again....")


run = RunInput()


