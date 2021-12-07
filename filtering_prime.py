def prime(number):
    prime_number = True
    for i in range(2,number):
        if number % i == 0:
            prime_number = False
    return prime_number

def filter_primes(list1):
    list2 = []
    for i in list1:
        if prime(i):
            list2.append(i)
    return list2