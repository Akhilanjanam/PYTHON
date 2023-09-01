#Write A Python Program To Check Duplication of Student Identity In A  Student List


sid=[]
print('enter id ')
for i in range(4):
    sid.append(int(input()))
x=set(sid)
if len(x)==len(sid):
    print('No duplication')
else:
    print('Duplication')
            
    
