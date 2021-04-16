#num1=int(input("enter the number "))
#for i in range(2,num1):
#   if(num1%i==0):
#      num="prime no"
# else:
#    num="not a prime"
#print(num)

num=int(input("enter the number "))
for i in range(2,num):
    if(num%i==0): #not prime
        flag=1
        break
    else:
        flage=0 #prime
if(flag>0):
    print("not prime")
else:
    print("prime")
