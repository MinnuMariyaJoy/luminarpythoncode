employee=[[1001,"arun",15000],
          [1002,"arjun",20000],
          [1003,"binu",13000]]
#print(employee)
#nested list - list inside list

# #for getting each element
# for i in employee:
#     print(i)
#

# #for collecting only names
# for i in employee:
#     print(i[1])
#


 #print employee name whose salary greter than 17000
# for i in employee:
#     if(i[2]>17000):
#         print(i[1])
#

#calculate total salary

total=0
for i in employee:
    total=total+i[2]
print(total)


