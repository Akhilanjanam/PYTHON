#Write A Python Program To Generate Number From 0 To 20 Only Even Number And  Generate 0 To 20 Odd Number. Add Both Generated Number To Each Other To Display Total Result 


ev=0
od=0
#print('number : ')
for i in range(0,21):
    if i%2==0:
        ev=ev+i
        #print(i)
for i in range(0,21):
    if i%2==1:
        od=od+i
       # print(i)
print('sum of even no : ',ev)
print('sum of odd no : ',od)
print('sum of odd no and evn no : ',ev+od)


