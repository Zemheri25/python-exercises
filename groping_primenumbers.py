range1 = int(input("Please enter your nmuber : "))
list1 = []
for i in range(range1):
    count = 0
    for ii in range(1, i+1):
        if i % ii == 0:
           count += 1
    if count == 2:
        list1.append(i)


number = int(input("Please enter your number : "))
list2 = []
if number == 2:
    for i in list1:
        for j in list1[list1.index(i)+1:]:
            if abs(i - j) == 6:
                tuple1 = (i,j)
                list2.append(tuple1)
elif number == 3:
    for i in list1:
        for j in list1[list1.index(i)+1:]:
            for h in list1[list1.index(j)+1:]:
                if abs(i-j) == 6 and abs(j-h) == 6:
                    tuple1 = (i,j,h)
                    list2.append(tuple1)


print(list2)