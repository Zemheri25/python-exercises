x = input("Please enter your first number : ")
y = input("Please enter your second number : ")
cons = (x, y)

def car (tuple12):
    return tuple12[0]


def cdr(tuple12):
    return tuple12[-1]

a = car(cons)
b = cdr(cons)

print(b)
print(a)
