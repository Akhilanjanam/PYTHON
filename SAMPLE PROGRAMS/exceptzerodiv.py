class Division:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def findDiv(self):
        try:
            div=self.num1/self.num2
            
        except ZeroDivisionError:
             print("zero division error")
             self.num2=int(input('number '))
             div=self.num1/self.num2
        return div     
n=int(input("number's : "))
n1=int(input())
a=Division(n,n1)
print('division ',a.findDiv())
