maths=int(input("enter your marks for maths "))
social=int(input("enter your marks for social "))
mala=int(input("enter your makrs for mala "))
eng = int(input('enter your marks for eng '))
total=maths+social+mala+eng
pg=total/200*100
print("your percentage is ",pg)
if(pg>=90):
    print("you scored A + ")
elif(pg>=80)&(pg<90):
    print("you scored A")
elif(pg>=70)&(pg<80):
    print("you scored B+")
elif(pg>=60)&(pg<70):
    print("you scored B")
elif(pg>=50)&(pg<60):
    print("you scored C+")
elif(pg>=40)&(pg<50):
    print("you scored C")
else:
    print("you have failed")
