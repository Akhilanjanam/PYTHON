#Write A Python Program To Get Two Number And Operator From The User To Perform Arithmetic Operation

a=int(input('first number : '))
b=int(input('second number : '))
opr=str(input('input the operator : '))
if(opr=='+'):
    print('sum = ',a+b)
elif (opr=='-'):
    print('difference = ',a-b)
elif(opr=='*'):
    print('product = ',a*b)
elif(opr=='/'):
    print('divison = ',a/b)
elif(opr=='%'):
    print('modulus = ',a%b) 
else:
    print('invalid operator')
            
    