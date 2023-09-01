#Write A Python Program To Take Age From The User To Check Whether User Able To Participate In Voting Or Not. If Age Is Less Than 18 Then It Don’t Allow To Participation. And Show, After How Much Year A Person Will Be Able To Participate:



age=int(input('Enter your age : '))
if age>18:
    print('You are eligible')
else:
    print('Sorry! you cannot participate in voting, you will be able to participate after {} years'.format(18-age))
