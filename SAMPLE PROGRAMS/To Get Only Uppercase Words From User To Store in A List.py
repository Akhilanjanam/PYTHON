#Write A Python Program To Get Only Uppercase Words From User To Store in A List 


lst = []
for i in range(10): 
    wrd= input("Enter the word : ")
    if(wrd.isupper()):
        lst.append(wrd)
    else:
        print("not in Uppercase ")
print(lst)