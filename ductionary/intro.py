#dictionary

dic={}
#print(type(dic))
#Key -value pairs
#roll:1098
#name:arun
#age:25

#key:rolls,name,age
#value:1098,arun,25

# student={"roll":1089,"name":"arun","age":25}
# print(student)
# #heterogenous values are allowed

student1={"rolls":1089,"name":"arun","age":25,"age":30,"cpp":25}
##print(student1)
#will not support duplicated key
#Dupliacted values will be supported

##for fectching a particular value use key
#print(student1["age"])

#roll:1089
#name
#age

for i in student1:
    print(i,",",student1[i])
    #print(i)
    #print(student1[i])

#for upadating name
student1["name"]="arjun"
student1["age"]=30
student1["cpp"]+=10
print(student1)

#for deleting a key and its corresponding value

#del student1["cpp"]
#print(student1)

#for adding a new key and a value
#total 150
#for checking a key in dictionary
# print("total" in student1)                           #very imported..for checking a key in the dictonary
# print("cpp" in student1)

#for adding elemnt
print(student1)
student1["total"]=158
print(student1)



