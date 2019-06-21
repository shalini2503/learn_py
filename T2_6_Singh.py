# Calculating projected tuition fees in dollars
class TuitionFees:
    tuition = 0
    no_of_years = 0

# Constructor function
    def __init__(self, tuition, no_of_years):
        self.tuition = tuition
        self.no_of_years = no_of_years

# calculating projection of  tuition fees for next five years
    def tuition_cal(self):
        print('Year', "\t", 'Projected Tuition(per Semester')
        print('-------------------------')
        for i in range(self.no_of_years):
            self.tuition += .03 * self.tuition
            # display result
            print(i+1, "\t\t", round(self.tuition, 2))


tf = TuitionFees(5333, 5)
tf.tuition_cal()
