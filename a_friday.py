__author__ = 'isaac'

"""

Written By: Gil Rael

The following program prints the A Friday - Fridays that are scheduled days off in 2017
the program takes the first A Friday off in January 2017 and then then calculates the other A Fridays
in 2017 based on this initial date


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
        self.initial_a_friday_date = (1, 6, 17)
        print("WTH")
        for item in self.initial_a_friday_date:
            print(item)
            print("Testing printing")
#    def __str__(self):



def main():
        new_date = AFriday()

if __name__ == "__main__":
        main()
