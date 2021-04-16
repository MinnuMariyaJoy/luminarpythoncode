class College:
    collegename="LT"
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
    def print(self):
        print("college name: ",College.collegename)
        print("NAme of student :",self.name)
        print("Roll no: ",self.roll)
    def __str__(self):
        return self.name+str(self.roll)
obj=College("Minnu",36)
print(obj)