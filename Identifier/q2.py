held = int(input("number of classes held"))
attenteded = int(input("number of classes attended"))
temp=(attenteded/held)*100
#print(temp)
if(temp>75):
    print("you are eligible")
else:
    print("you are not eligible")