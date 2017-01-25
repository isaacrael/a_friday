__author__ = 'isaac'

"""

Written By: Gil Rael

The following program prints the A Friday - Fridays that are scheduled days off in 2017,
The program takes the hard coded first A Friday that is a scheduled day off in January 2017
and then calculates the other A Fridays in 2017 based on this initial date.


Planning

Modules Needed

from datetime import *

Classes

A_Friday

Attributes                                           Methods
                                                     def_init__(self):
# hard coded                                         def__str__
initial_a_friday_date -> str                         def calculate_a_friday(self):
a_friday = initial_a_friday_date + 14 days

"""

from datetime import *


class AFriday(object):
    def __init__(self):
        self.counter = 0
        self.initial_a_friday_date = "1/6/17"
        print("\nThe A Friday Dates In The Year 2017:\n")
        self.initial_a_friday_date = datetime.strptime(self.initial_a_friday_date, "%m/%d/%y")
        print(self.initial_a_friday_date)
# For testing purposes        print(self.date_1.year)
# For testing purposes        int(self.date_1.year)
        self.next_a_friday_date = self.initial_a_friday_date + timedelta(days=14)
        print(self.next_a_friday_date)
        while (self.counter < 24):
            self.counter = self.counter  + 1
            self.next_a_friday_date = self.next_a_friday_date + timedelta(days=14)
            print(self.next_a_friday_date)


def main():
# creates and AFriday object
        new_date = AFriday()


if __name__ == "__main__":
        main()
