# program to calculate the weekly sales of a store using list data structure
import locale


# class to manage weekly sales of a store in list
class StoreSales:
    sales = []
    locale.setlocale(locale.LC_ALL, '')

    # constructor function
    def __init__(self):
        self.sales = [0] * 7

    # stores per day sales in a list
    def add_sales(self, val):
        self.sales.append(val)

    # calculates the sum of the list using loop
    def calculate_total_weekly_sales(self):
        total = 0
        for sale in self.sales:
            total += sale
        return total

    # prints the weekly sales by calling "calculate_total_weekly_sales()" function
    def print_total_sales(self):
        print("Total sales for the week: ", locale.currency(self.calculate_total_weekly_sales(), grouping=True))


# this class is used to run stdio for this program
class RunInput:
    # constructor function
    def __init__(self):
        days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        while True:
            # ask user to input the sales per day
            try:
                sales = StoreSales()
                for i in range(0, len(days)):
                    sales.add_sales(float(input("Enter the sales for "+days[i]+": ").strip()))
                sales.print_total_sales()
                print()
            except ValueError:
                print("Invalid value provided. Try again...")
            except:
                print("please try again....")


run = RunInput()
