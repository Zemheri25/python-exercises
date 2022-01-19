mylist = [-1, -2, 1, 2 ,3, 4, 5,6, 7]
newlist = []
newlist2 = []
for i in range(min(mylist), max(mylist)):
    newlist.append(i)

for i in newlist:
    if i not in mylist:
        newlist2.append(i)

if len(newlist2) > 0 and max(newlist2) > 0:
    print(max(newlist2))
else :
    print(max(mylist)+1)
