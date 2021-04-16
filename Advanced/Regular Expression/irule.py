#for chechikng whether the word is 6 letter word
import re
n="hellooo"
x='\w{6}'

match=re.fullmatch(x,n)
if match is not None:
    print("valid")

else:
    print("Invalid")