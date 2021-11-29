list1 = []
for i in range(100):
    count = 0
    for ii in range(1, i+1):
        if i % ii == 0:
           count += 1
    if count == 2:
        list1.append(i)


print(list1)




def prime_number(range1):
    list1 = []
    for i in range(range1):
        count = 0
        for ii in range(1, i+1):
            if i % ii == 0:
                count += 1
        if count == 2:
            list1.append(i)
    return list1

print(prime_number(int(input("Please enter your number : "))))






list1 = []
number = 20
for i in range(2, number+1):
    a = [ii for ii in range(1, i+1) if i % ii == 0]
    if len(a) == 2:
        list1.append(i)
print(list1)