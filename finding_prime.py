def prime_number(number):
    prime = True
    for i in range(2, number):
        if number % i == 0:
                prime = False
    return prime

list1 = []
number1 = int(input("Please enter your number : "))
for i in range(number1, 100):
    if prime_number(i):
        list1.append(i)

print(min(list1))