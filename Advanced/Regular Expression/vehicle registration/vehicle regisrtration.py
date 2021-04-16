import re
lst=[]
f=open("vehicle","r")
x='\w{2}\d{2}\w{2}\d{4}'     #"[Kk][Ll]\d{2}[a-zA-Z]{2}\d{4}
for num in f:
    number=num.rstrip("\n")
    matcher = re.fullmatch(x,number)
    if matcher is not None:
        lst.append(number)
print(lst)