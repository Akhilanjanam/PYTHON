#Write A Python Program That Accepts Six Identity Numbers Of Students As Input And Display In Descending Order

lst=[]
print('Identity number : ')
for i in range(3):
    lst.append(int(input()))
lst.sort(reverse=True)
print(lst)

