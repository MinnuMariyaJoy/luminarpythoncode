
age=int(input("enter your age"))
if(age>50):
    salary=int(input("enter your salary"))
    bonus= .05*salary
    newsalary=salary+bonus
    print("your  new net salary is ",newsalary)
else:
    print("no change in salary")
