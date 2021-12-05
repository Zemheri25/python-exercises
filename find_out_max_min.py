list1 = []
size = int(input("How many numbers will you enter ? : "))
for i in range(size):
    number = int(input("Please enter your number : "))
    list1.append(number)
list1 = list(map(abs, list1))


def max_product(list1):
    list2 = []
    list1.sort()
    for i in list1[-1:-4:-1]:
        list2.append(i)
    count = 1
    for j in list2:
        count *= j
    return count


def min_product(list1):
    list3 = []
    list1.sort()
    for i in list1[:3]:
        list3.append(i)
    count = 1
    for j in list3:
        count *= j

    return count

print(max_product(list1))
print(min_product(list1))