#Write A Python Program To Create A File And Write User Name, And Age In That File


file = open("nameage.txt","w+")
name = input("Name : ")
age = input("Age : ")
file.write("Your name is "+str(name))
file.write("Your age is "+str(age))
file.close()