__author__ = 'isaac'

"""

Written By: Gil Rael

The following program prints the A Friday - Fridays that are scheduled days off in 2017
the program takes the first A Friday off in January 2017 and then then calculates the other A Fridays
in 2017 based on this initial date


Planning

Modules Needed

from datetime import *
from calendar import *

Classes

A_Friday



Attributes                                           Methods

                                                     def_init__(self):
# hard coded                                         def__str__
initial_a_friday_date -> str                         def calculate_a_friday(self):
a_friday = initial_a_friday_date + 14 days



"""

from datetime import *
from calendar import *


class AFriday(object):
    def __init__(self):
        self.initial_a_friday_date = "1/6/17"
        self.increment = 0
        print("The A Friday dates in the year 2017 are\n")
        self.date_1 = datetime.strptime(self.initial_a_friday_date, "%m/%d/%y")
        print(self.date_1)
        while (self.increment < 12):
            self.increment = self.increment  + 1
            self.next_a_friday_date = self.date_1 + timedelta(days=14)
            print(self.next_a_friday_date)
            self.next_a_friday_date = self.next_a_friday_date + timedelta(days=14)
            print(self.next_a_friday_date)


#    def __str__(self):



def main():
        new_date = AFriday()


if __name__ == "__main__":
        main()
