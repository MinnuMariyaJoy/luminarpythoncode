# #add numbers()
# #snake notation add_twonumbers
# #camelnotation addTwo
#
#
# add=lambda num1,num2:num1+num2
# print(add(200,300))
#
#
# # def cube(num):
# #     return num**3
#
#
# cube=lambda num:num**3
# print(cube(3))



#map()
#filter()
#reduce()


# lst=[10,20,30,21,22]
# squ=[]
# for num in lst:
#     res=num**2
#     squ.append(res)
# print(squ)
#

#map - if we waant to perform a function on each object
# two arguemnts should be there, enthu ftn aanu...eethu fnt nu aanu apply cheyyan ponathu
# lst=[10,20,30,21,22]
# def squ(no):
#     return no**2
# squres = list(map(squ,lst))
# print(squres)


lst=[10,20,30,21,22]
squres=list(map(lambda no:no**2,lst))
print(squres)

#2 argument
#1)fuction?
#2)iterables

lst=[10,20,2,3,45]
cubes=list(map(lambda no:no**3,lst))
print(cubes)


