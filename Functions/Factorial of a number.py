#5!=5*4*3*2*1
# def factorial():
#     num=int(input("enter your number"))
#     fact=1
#     for i in range(1,(num+1)):
#         fact=fact*i
#     print(fact)
# factorial()


# def factorial(num1):
#     fact=1
#     for i in range(1,(num1+1)):
#         fact=fact*i
#     print(fact)
# factorial(3)


def factorial(num):
    fact=1
    for i in range (1,(num+1)):
        fact=fact*i
        return(fact)
data=factorial(5)
print(data)