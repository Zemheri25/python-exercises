list1 = []
size = int(input("How many numbers are you gonna enter : "))
for i in range(size):
    number = int(input("Please enter your number : "))
    list1.append(number)

def repeat(list1, number):
    a = list1.copy()
    list1.extend(a*number)
    return list1

def add(list1, number):
    list1.append(number)
    return list1

def remove(list1, number1, number2,):
    for i in list1[number1: number2+1]:
        list1.remove(i)
    return list1

def concat(list1, list2):
    list1.extend(list2)
    return list1

print(repeat(list1, 2))
print(add(list1, 1))
print(remove(list1, 1, 12))
print(concat(list1, [3, 4]))