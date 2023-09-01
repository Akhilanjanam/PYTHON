#Write A Python Program To Get Name From User, To Check It Is In Uppercase Or Not, If Not Upper Then Convert Into Uppercase

name=input("enter the name : ")
if name.isupper():
    print('name is in upper case : ',name)
else:
    print(' name is converted to uppercase : ',name.upper())