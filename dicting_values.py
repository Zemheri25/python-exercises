size = int(input("How many numbers will you enter : "))
list1 = []
for i in range(size):
    number = input("PLease enter your number : ")
    list1.append(number)



def liste(list1):
    dict1 = {}
    for i in list1:
        if i not in dict1:
            dict1[i] = [i]
        else:
            dict1[i] += [i]
    return list(dict1.values())

print(liste(list1))