#Write A Python Program To Get A Number From User To Return Its Next Number With Addition Of User Entered Number And Previous Number With Addition Of User Entered Number

class number:
    def __init__(self,num):
        self.num=num
    def next_pre(self):
        self.num=int(input("Enter a number : "))
        nxtno=self.num+1+self.num
        prvno=self.num-1+self.num
        print('next no : ',nxtno)
        print('Previous no : ',prvno)
        return nxtno
        
x=number(2)
y=x.next_pre()
print('nxtno+10 : ',y+10)

