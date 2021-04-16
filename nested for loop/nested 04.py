#10 9 8 7 6 5 4 3 2 1
#9 8 7 6 5 4 3 2 1
#8 7 6 5 4 3 2 1
#7 6 5 4 3 2 1
#6 5 4 3 2 1
#
#
#1

for i in range(0,11):
    for j in range((11-i),0,-1):
        print(j,end=" ")
    print(" ")