# #filter(function ,iteration)
# lst=[2,3,45,20,10]
# even=list(filter(lambda no:no%2==0,lst))
# print(even)

lst=["akhil","aravind","akshay","varun","vipin","ram"]
aname=list(filter(lambda name:name[0]=="a",lst))
print(aname)