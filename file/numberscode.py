f=open("numbers","r")
lst=[]
for num in f:
    lst.append(int(num.rstrip("\n")))
print(sum(lst))
#print(sum)