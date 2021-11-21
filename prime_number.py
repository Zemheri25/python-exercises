list1 = []
number = int(input("Please enter your number : "))
for i in range(1, number+1):
    if number % i == 0:
        list1.append(i)
if len(list1) > 2:
    print(f"Your number {number} is not a prime number ")
else:
    print(f"Your number {number} is a prime number ")



def primenumber(x):
    list1 = []
    for i in range(1, x+1):
        if x % i == 0:
            list1.append(i)
    if len(list1) > 2:                                          #THİS SOLUTİON WİTH PYTHON FUNCTİON
        return (f"Your number {x} is not prime number. ")
    else:
        return (f"Your number {x} is prime number.")


print(primenumber(4))