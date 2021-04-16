import re
#minnumariyaj@gmail.com
n=input("enter your mail id")
x='([a-zA-Z0-9_+.-]+[@][a-zA-Z0-9]+\.[a-zA-Z0-9]+$)'
match=re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("invalid")