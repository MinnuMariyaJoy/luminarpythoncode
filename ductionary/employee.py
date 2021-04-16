#employee

#keys - id, emlpoyyee name,designation, salary

#1. print employee name only
#2. check whther compony key in employee
#3. add compony and luminar
#4.upadte salry =15k
#print all key value pairs

employee={"id":1890,"name":"Minnu","designation":"Tutor","Salary":15000}
print(employee)

print(employee["name"])
print("company" in employee)
employee["company"]="luminar"
print(employee)
employee["Salary"]+=15000
print(employee)
for i in employee:
    print(i, ",", employee[i])

