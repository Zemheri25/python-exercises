list1 = [1, 2, 3, 4, 5, 6, 7]
list2 = []
list3 = []
count1 = 0
count2 = -1
if len(list1) % 2 == 0:
        for i in range(round(len(list1)/2)):
            list2 = [list1[count1], list1[count2]]
            count1 += 1
            count2 -= 1
            list3.append(list2)
else:
    for i in range(round(len(list1)/2 + 0.1)):
        list2 = [list1[count1], list1[count2]]                 #THIS SOLUTİON WİTH NORMAL METHODS
        count1 += 1
        count2 -= 1
        list3.append(list2)

print(list3)




def pairs(list1):
    list2= []
    list3 = []
    count1 = 0
    count2 = -1
    if len(list1) % 2 == 0:
        for i in range(round(len(list1)/2)):
            list2 = [list1[count1], list1[count2]]
            count1 += 1
            count2 -= 1
            list3.append(list2)
    else:
        for i in range(round(len(list1)/2 + 0.1)):       #THIS SOLUTİON WİTH FUNCTİON
            list2 = [list1[count1], list1[count2]]
            count1 += 1
            count2 -= 1
            list3.append(list2)
    
    
    
    return list3

print(pairs([5, 9, 8, 1, 2, 4]))