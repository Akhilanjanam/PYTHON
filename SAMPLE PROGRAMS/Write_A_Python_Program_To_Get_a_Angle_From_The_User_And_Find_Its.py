#Write A Python Program To Get a Angle From The User And Find Its Sin And Cos Value In Radian


from math import sin
from math import cos
angle=float(input('enter an angle : '))
sres=sin(angle)
cres=cos(angle)
print('sin {} = '.format(angle),sres)
print('cos {} = '.format(angle),cres)