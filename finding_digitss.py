list1 = []
number = int(input("Please enter your number : "))
for i in range(1, number):
    list1.append(i)

a = list(map(str, list1))
b = "".join(a)
print(len(b))





list1 = []
def digits(number):
    for i in range(1, number):
        list1.append(i)

    a = list(map(str, list1))
    b = "".join(a)
    return len(b)
print(digits(int(input("Please enter your number : "))))
