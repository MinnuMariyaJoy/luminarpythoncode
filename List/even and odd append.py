lst=[]
odd=[]
even=[]

for i in range(0,51):
    lst.append(i)
print(lst)

for i in lst:
    if(i%2==0):
        even.append(i)
    else:
        odd.append(i)
print(even)
print(odd)