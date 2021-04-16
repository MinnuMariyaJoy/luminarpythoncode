lst=[4,2,1,6,7,8]

#output [3,1,0,7,8,9]

out=[]
for i in lst:
    if(i>5):
        i+=1
        out.append(i)
    else:
        i-=1
        out.append(i)
print(out)


