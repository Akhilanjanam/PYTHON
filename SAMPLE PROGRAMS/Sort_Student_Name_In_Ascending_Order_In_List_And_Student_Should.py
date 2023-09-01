#Write A Python Program To Sort Student Name In Ascending Order In List And Student Should Display Which Contain Only 5 Character


lst=['anu','minnu','fidha','aiswarya','chiathra','kiran']
lst.sort()
for i in lst:
    if len(i)==5:
        print(i)