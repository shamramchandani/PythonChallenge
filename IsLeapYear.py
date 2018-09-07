#This script ask the user for a Year and then decided is if it is a Leap Year or not 

year = int(input("Please Enter the Year in numbers"))

if year % 4 == 0:
    print('this is a leap year')
else:
    print('this is not a leap year')
