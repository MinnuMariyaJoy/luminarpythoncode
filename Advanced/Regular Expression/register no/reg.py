import re
f2=open("validreg",'w')
x='([L][U][M]\d{2}[P][Y]\d{3}$)'                          #LUM12PY678
f=open("reg no", "r")
  #if file doesnot exist use append, for existing files use w
for num in f:
    number=num.rstrip("\n")
    matcher= re.fullmatch(x,number)
    if matcher is not None:
        f2.write(number)
        f2.write('\n')

