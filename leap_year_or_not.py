# write a python program to check wheather the year is a leap year or not
v=int(input('Enter the year to be checked:-'))
if v%4==0 and v%100!=0 and v%400==0:
    print('the year is a leap year')
else:
    print('the year is not a leap year')