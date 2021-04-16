lst=[18,4,5]
index=int(input("enter the index"))
try:
    print(lst[index])
except:
    print("exception")
finally:
    print("inside finally") #finally block will be always working along with try block