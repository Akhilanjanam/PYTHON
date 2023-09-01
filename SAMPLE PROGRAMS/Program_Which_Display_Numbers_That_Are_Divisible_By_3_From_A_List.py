#Write A Python Program Which Display Numbers That Are Divisible By 3 From A List


lst=[]
print('Numbers : ')
for i in range(5):
    lst.append(int(input()))
print('Numbers That Are divisible by 3 : \n')
for i in lst:
    if(i%3==0):
        print(i)