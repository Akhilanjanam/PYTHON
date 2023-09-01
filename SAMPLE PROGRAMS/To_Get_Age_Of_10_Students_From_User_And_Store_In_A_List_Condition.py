#Write A Python Program To Get Age Of 10 Students From User And Store In A List. Condition Is That, System Should Display Age That Greater Than 14 Year And Less Than 20 Year 


age=[]
print("Enter the age of students : ")
for i in range(1,4):
    age.append(int(input()))
print('Age That Greater Than 14 Year And Less Than 20 Year : ')
for i in age:
    if(i > 14 and i < 20):
        print(i)
        
        
