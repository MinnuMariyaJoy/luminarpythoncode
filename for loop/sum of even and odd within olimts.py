lower=int(input('enter the lower limit'))
upper=int(input("enter the upper limit"))
sume=0
sumo=0
for i in range(lower,(upper+1)):
    if(i%2==0):
        sume=sume+i
    if(i%2==1):
        sumo=sumo+i
print("sum of even is ",sume)
print("sum of odd is ",sumo)