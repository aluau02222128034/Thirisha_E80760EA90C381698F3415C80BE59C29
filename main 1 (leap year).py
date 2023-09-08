# Leap Year
"""
year % 4==0 &
year % 100!=0/
year % 400==0

"""


def isleapYear(year):
  return bool(year % 4 == 0 and year % 100 != 0 or year % 400 == 0)


year = int(input("Enter the year :"))

if isleapYear(year):
  print('{} is a leap year.'.format(year))
else:
  print('{} is not a leap year.'.format(year))
