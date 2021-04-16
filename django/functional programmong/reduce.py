from functools import reduce
lst=[10,20,30,50,80]
total=reduce(lambda no1,no2:no1+no2,lst)
max=reduce(lambda no1,no2:no1 if no1>no2 else no2,lst)
min=reduce(lambda no1,no2:no1 if no1<no2 else no2,lst)
print(total)
print(max)
print(min)


# if (no<0):
#     return -ve
# else:
#     return +ve
# n1 if n1>n2 else no2