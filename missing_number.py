size = int(input("How many numbers will you enter ? : "))
list1 = []
for i in range(size):
    number = int(input("Please neter your number : "))
    list1.append(number)


list1.sort()
list2 = [i for i in range(min(list1), max(list1))]
diffrences = [i for i in list2 if i not in list1]

pozitif = min([i for i in diffrences if i > 0])
print(pozitif)