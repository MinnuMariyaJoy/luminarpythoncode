f=open("numbers","r")
lst=[]
even=[]
odd=[]
for num in f:
    lst.append(int(num.rstrip("\n")))
for number in lst:
    if(number%2==0):
        even.append(number)
    else:
        odd.append(number)

print(sum(odd))
print(sum(even))


