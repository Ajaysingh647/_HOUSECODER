# write a program to input any character and check whether it is alphabet, digit and special character.
v=int(input('Enter the character:-'))
if(v>='a' and v<='z') and (v>='A' and v<='Z'):
    print('The character are alphabates')
elif v>=0:
    print('the character are digit')
else:
    print('the character are special character')