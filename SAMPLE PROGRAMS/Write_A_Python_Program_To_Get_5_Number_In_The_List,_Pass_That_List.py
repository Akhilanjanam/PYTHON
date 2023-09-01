#Write A Python Program To Get 5 Number In The List, Pass That List In The Function To Multiply And Add That Number And Display Total Result

lst=[]
for i in range(0,4):
    lst.append(int(input('enter the no : ')))
def arithop(num):
    add=0
    mul=1
    for i in num:
        add=add+i
        mul=mul*i
    print('sum =',add)
    print('product =',mul)
arithop(lst)        