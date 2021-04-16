lst=[4,2,1,6,7,8]

#output [3,1,0,7,8,9]

otputlist=[]
for i in lst:
    if(i>5):
        i+=1
    otputlist.append(i)
    else:
    i -= 1
    otputlist.append(i)




print(otputlist)