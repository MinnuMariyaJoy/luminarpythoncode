#combination of upper case and lower case ending with a number

import re
n=input("word")
x='[a-zA-z]+[0-9]+$'
match=re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("invalid")



