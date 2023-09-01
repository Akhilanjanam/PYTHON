#Write A Python Program To make a average calculator. 


lst=[]
l=int(input('enter the limit : '))
print('amount :')
for i in range(l):
    lst.append(int(input()))
avg=sum(lst)/l
print('Average = ',avg)