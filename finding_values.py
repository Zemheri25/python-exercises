size = int(input("How many numbers will you enter ? : "))
list1 = []
for i in range(size):
    number = int(input("Please enter yuor nmuber : "))
    list1.append(number)

list2 = []
list3 = []
looking = int(input("Please enter your looking : "))
for i in list1:
    for j in list1[list1.index(i) + 1:]:
        if i * j == looking:
            list2 = [i,j]
            list2.sort()
            list3.append(list2)
        
for i in list3:
    print(i, end=' ')