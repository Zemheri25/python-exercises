list3 = []
list2 = []   
list1 = ("Chris Pratt", ["chirps", "rat"])
for i in list1[0]:
    list2.append(i)
for i in list1[1]:
    for j in i:
        list3.append(j)

list2 = sorted([i.lower() for i in list2 if i.isalpha()])
list3 = sorted([i.lower() for i in list3 if i.isalpha()])    

if list2 == list3:
    print(True)
else:
    print(False)
