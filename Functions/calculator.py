print("press 1 for addition")
print("press 2 for sub")
print("press 3 for mul")
print("press 4 for dividion")
option=int(input("enter your option"))
num1=int(input("enter no 1"))
num2=int(input("enter no 2"))
def add():
    result1=num1+num2
    print(result1)
def sub():
    result2=num1-num2
    print(rsult2)
def mul():
    result3=num1*num2
    print(result3)
def division():
    result4=num1/num2
    print(result4)
if(option==1):
    add()
elif(option==2):
    sub()
elif(option==3):
    mul()
elif(option==4):
    division()
else:
    print("error")




# def add(num1,num2):
#     return num1+num2
# def sub(num1,num2):
#     return num1-num2
# def mul(num1,num2):
#     return num1*num2
# def div(num1,num2):
#     retunr num1/num2
#
# print("select operations\n"
#       "1.add\n"
#       "2.sub\n"
#       "3.mul\n"
#       "4.div")
# select=int(input("select operation"))
# num1=int(input("eneter first number"))
# num2=int(input("enter second number"))
# if select==1
#     print(num1,"+",num2,"=",add())