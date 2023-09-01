#Write A Python Program To Get Name From A List, That Ends At ‘n'


lst=[]
print("enter the Name : ")
for i in range(3):
    lst.append(input())
print('Name : ')
for i in lst:
    if i[-1]=='n':
        print(i)
    