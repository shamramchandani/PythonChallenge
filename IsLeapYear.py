#This script ask the user for a Year and then decided is if it is a Leap Year or not 
import sys
try:
    year = int(input("Please Enter the Year in numbers "))
except ValueError:
    print('You have to enter numbers only')
    sys.exit()

if year % 4 == 0:
    print('this is a leap year')
else:
    print('this is not a leap year')
