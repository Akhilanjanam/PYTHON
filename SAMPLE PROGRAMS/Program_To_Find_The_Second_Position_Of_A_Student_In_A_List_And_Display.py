#Write A Python Program To Find The Second Position Of A Student In A List. And Display Marks


marks=[] 
print('enter the mark')
for i in range(5):
    marks.append(int(input()))
marks.sort(reverse=True)
print('marks',marks)
print("Second Position = ",marks[1])