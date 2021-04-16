# def add(*args):  #tuple format
#     sum=0
#     for num in args:
#         sum+=num
#     return sum
# res=add(20,20,30)
# print(res)







# def print_person_details(*args):
#     print(args)
# print_person_details("ajay","coder",26)


#
# def print_person_details(**kwargs):
#     print(kwargs)
# print_person_details(name="ajay",job="coder",age=26)




# *args - tuples
# **kwargs - dictionary(key value pair)



# lst=[10,34,20,76,4,30,5]
# lst=sorted(lst,reverse=False)
# print(lst)








# employees={
#     1000:{"name":"Minnu","design":"trainer","exp":3},
#     1001:{"name":"arun","design":"trainer","exp":2},
#     1002:{"name":"neha","design":"trainer","exp":3}
# }
#
# eid=int(input("enter the employee id "))
# if eid in employees:
#     print("eid exist")
#     print(employees[eid]["name"])
# else:
#     print("edi dosent exist")
















#crwate a function

employees={
    1000:{"name":"Minnu","design":"trainer","exp":3},
    1001:{"name":"arun","design":"trainer","exp":2},
    1002:{"name":"neha","design":"trainer","exp":3}
}
id=int(input("enter id"))
#emp_details(eid=1000)    #sanjay

def emp_details(**kwargs):     #kwargs={eid:1000}
    id=kwargs["eid"]
    if id in employees:
        print(employees[id]["name"])
    else:
        print("desnt exist")






