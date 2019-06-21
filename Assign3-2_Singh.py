# program to calculate the property tax
import locale


class PropertyTax:
    actual_cost = 0
    percent_on_actual = .60
    assessment_value = 0
    property_tax = 0
    tax_factor = .72
    locale.setlocale(locale.LC_ALL, '')

    # constructor function
    def __init__(self, cost):
        self.actual_cost = cost

    # calculating the assessment value and property tax
    def cal_tax(self):
        self.assessment_value = self.percent_on_actual * self.actual_cost
        self.property_tax = self.tax_factor * (self.assessment_value/100)
        # display
        print("Assessed value :", locale.currency(self.assessment_value, grouping=True))
        print("Property tax:", locale.currency(self.property_tax, grouping=True))


# this class is used to run stdio for this program
class RunInput:
    # constructor function
    def __init__(self):
        while True:
            # ask user to input the actual value of property in dollars
            try:
                cost = float(input("Enter the actual value").strip())
                property_tax = PropertyTax(cost)
                property_tax.cal_tax()
            except ValueError:
                print("Invalid value provided. Try again...")
            except:
                print("please try again....")


run = RunInput()




