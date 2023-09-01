#Write Python Program To Get A Username From The User That Should Have Alphanumeric Characters, Then Pass That Username To Function As Parameter, To Display That Username


uname=input('UserName : ')
def username(a):
    if a.isalnum():
        return('your username is {}'.format(uname))
    else:
         return('wrong username')  
username(uname)