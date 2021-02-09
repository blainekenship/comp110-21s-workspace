"""A vaccination calculator."""

__author__ = "730400756"

# The datetime data type is imported from the datetime library.
# A datetime object models a specific date and time.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime-objects
from datetime import datetime

# The timedelta data type is imported from the timedelta library.
# A timedelta object models a "time span", such as 1 day or 1 hour and 3 minutes.
# Subtracting two datetime objects will result in the timedelta between them.
# Adding a datetime and a timedelta will result in the datetime offset by the timedelta.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime.timedelta
from datetime import timedelta


# Begin your solution here...
Pop: int = int(input("Total number of people under consideration: "))
Admin: int = int(input("Total number of vaccines already administered to the population: "))
Per_Day: int = int(input("Total number of vaccines to be given hence forth per day: "))
Percent: int = int(input("Percent of people you would like to see vaccinated: "))

today: datetime = datetime.today()


print("Population: " + str(Pop))
print("Doses administered: " + str(Admin))
print("Doses per day: " + str(Per_Day))
print("Target percent vaccinated: " + str(Percent))
print("We will reach")