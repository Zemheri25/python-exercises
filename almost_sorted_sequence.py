list2 = []
list1 = [6, 4, 2, 0]
if list1[0] < list1[1]:  
    for i in range(len(list1)-1):
        if list1[i] < list1[i+1] and list1[-1] > list1[-2]:
            list2.append(False)
        else:
            list2.append(True)
else:
    for i in range(len(list1)-1):
        if list1[i] > list1[i+1] and list1[-1] < list1[-2]:
            list2.append(False)
        else:
            list2.append(True)

print(any(list2))
print(list2)    





def almost_sorted(list1):
    list2 = []
    if list1[0] < list1[1]:
        for i in range(len(list1)-1):
            if list1[i] < list1[i+1] and list1[-1] > list1[-2]:
                list2.append(False)
            else:
                list2.append(True)
    else:
        for i in range(len(list1)-1):
            if list1[i] > list1[i+1] and list1[-1] < list1[-2]:
                list2.append(False)
            else:
                list2.append(True)
    
    return (any(list2), list2)

print(almost_sorted([6, 4, 2, 0]))