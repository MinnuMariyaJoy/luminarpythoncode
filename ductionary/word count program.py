line="hai hello hai hello hai"
#hai 3 times
#hello - 2 times

#split function - for splitting a line in to word by word

#print(line)
#for splitting
word=line.split(" ")
print(word)

dic={}
for i in word:
    if (i not in dic):
        dic[i] = 1
    else:
        dic[i]+=1
print(dic)

