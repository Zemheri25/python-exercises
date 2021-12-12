number = int(input("Please enter your number : "))
list1 = []
if number % 2 == 0:
    list1.append(number /2)
else:
    list1.append(number*3+1)    
while list1[-1] != 1:
    if list1[-1] %2 == 0:
        list1.append(int(list1[-1] / 2))
    else:
        list1.append(int(list1[-1]*3+1))                       #THIS SOLUTİON WİTH NORMAL METHODS

a = len(list1)
b = max(list1)
list2 = [a, b]
print(list2)





def collatz(number):
    list1 = []
    if number % 2 == 0:
        list1.append(number / 2)
    else:
        list1.append(number*3+1)

    while list1[-1] != 1:
        if list1[-1] % 2 == 0:
            list1.append(int(list1[-1] / 2))
        else:
            list1.append(int(list1[-1]*3+1))               #THIS SOLUTİON WİTH DEF FUNCTİON
    a = len(list1)
    b = max(list1)
    list2 = [a, b]
    return list2

print(collatz(17))