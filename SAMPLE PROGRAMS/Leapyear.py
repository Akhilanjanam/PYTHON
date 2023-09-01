#Write A Python Program To Check A Year, Whether It Is Leap Year Or Not


yr=int(input("ente a year: "))
if((yr%400==0)or(yr%4==0 and yr%100!=0)):
    print('Leap year')
else:
    print('Not a Leap year')    