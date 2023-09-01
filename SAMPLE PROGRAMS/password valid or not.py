# Write Python Program To Get Password From User And Make Sure That Password Should Contain Number And Alphabetic 
 

list=[]
s=input("Enter ")
if (len(s)>=8):
    for i in s:
        if i.isupper():
            list.append(i)
        if i.islower():
            list.append(i)
        if i.isdigit():
            list.append(i)
    if (len(list)==len(s)):
        print("valid password")
    else:
        print("invalid password")
