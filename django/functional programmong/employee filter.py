class Employee:
    def __init__(this,eid,ename,desig,salary):
        this.eid=eid
        this.ename=ename
        this.desig=desig
        this.salary=salary
    def print_emp(this):
        print(this.ename)
e1=Employee(1089,"Minnu","developer",290000)
e2=Employee(1010,"arun","developer",250000)
e3=Employee(1025,"vivek","qa",280000)
e4=Employee(1011,"athul","marketing",270000)

employees=[]
employees.append(e1)
employees.append(e2)
employees.append(e3)
employees.append(e4)

developers=list(filter(lambda emp: emp.desig=="developer",employees))
for dev in developers:
    print(dev)
