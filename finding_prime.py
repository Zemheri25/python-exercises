def prime_number(number):
    prime = True
    for i in range(2, number):
        if number % i == 0:
                prime = False
    return prime

list1 = []
number1 = int(input("Please enter your number : "))
for i in range(number1, 100):
    if prime_number(i):                                     #THİS SOLUTİON WİTH NORMAL METHODS
        list1.append(i)

print(min(list1))

def next_prime(number1):
    number1 = int(input("Please enter your number : "))
    list1 = []
    for i in range(number1, 100):
        if prime_number(i):                               #THİS SOLUTİON WİTH FUNCTİON
            list1.append(i)

    return min(list1)

print(next_prime("number"))