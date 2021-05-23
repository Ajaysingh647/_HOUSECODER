# write a python program to find the maximum between three number.
v=int(input('enter the first number:-'))
a=int(input('enter the second number:-'))
n=int(input('enter the third number:-'))
if v>a and v>n:
    print(f'The {v} is greater than {a} and {v} is greater than {n}')
    print(f'Largest number is {v}')

elif a>v and a>n:
    print(f'The {a} is greater than {v} and {a} is greater than {n}')
    print(f'Largest number is {a}')
else:
    print(f'The {n} is greater than {v} and {n} is greater than {a}')
    print(f'Largest number is {n}')


