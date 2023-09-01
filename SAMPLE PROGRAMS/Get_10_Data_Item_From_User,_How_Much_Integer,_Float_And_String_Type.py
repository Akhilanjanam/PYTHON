#Write A Python Program To Get 10 Data Item From User, How Much Integer, Float And String Type Of Data Is Stored In A List


data=['anu',7,'52','minnu',2,3,2.5,8.5]
integer=0
floatno=0
string=0
for i in data:
    if(type(i)==int):
        integer=integer+1
    if(type(i)==float):
        floatno=floatno+1
    if(type(i)==str):
        string=string+1
print('integer : ',integer)
print('float : ',floatno)
print('string : ',string)