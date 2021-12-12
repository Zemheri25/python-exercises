def prime_number(number):
    prime = True
    for i in range(2, number):
        if number % i == 0:
            prime = False

    return prime

def is_primes(value, number):
    if value == "prime" and prime_number(number):
        return "Yes"
    elif value == "prime" and not prime_number(number):
        return "No"
    else:
        "Nonvalid"

print(is_primes("prime", 5))
print(is_primes("prime", 4))