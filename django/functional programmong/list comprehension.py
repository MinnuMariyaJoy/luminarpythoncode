# lst=[1,2,3,4]
# lst2=[10,20]
# output=[]
# for i in lst:
#     for j in lst2:
#         output.append((i,j))
# print(output)




lst=[1,2,3,4]
square=[num**2 for num in lst]
even=[num for num in lst if num%2==0]
print(even)
print(square)