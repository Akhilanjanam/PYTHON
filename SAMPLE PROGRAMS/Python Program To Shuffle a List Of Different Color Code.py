#Write A Python Program To Shuffle a List Of Different Color Code

import random
color=[]
print('enter color')
for i in range(5):
    color.append(input())
random.shuffle(color)
print(color)