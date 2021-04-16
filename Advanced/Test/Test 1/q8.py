#finally block will be always working along with try block

a=int(input("enter your first no"))
b=int(input("enter your second no"))
try:
    c=a/b
    print("sum = ",c1)
except:
    print("Error")
finally:
    print("process completed")