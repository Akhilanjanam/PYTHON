#Write A Python Program To Find Sum Of Two Number (That Number Should Be Positive  And Less Than 50)


n1 = int(input("Enter first number : "))
n2 = int(input("Enter second number : "))

if((n1>0 and n2>0) and (n1<50 and n2<50)):
    print("sum : ",n1+n2)
else:
    print("Given number should be positive and less than 50")