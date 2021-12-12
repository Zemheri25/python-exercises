list2 = []
number = int(input("Please enter your number : "))
for i in range(1, number):
    if number % i == 0:
        list2.append(i)

if sum(list2) == number:
    print("perfect")

list3 = []
y = sum(list2)
for i in range(1, y):                                  #THIS SOLUTION WİTH NORMAL METHODS
    if y % i == 0:
        list3.append(i)

if sum(list3) == number:
    print("amicaple")



def num_type(number):
    list3 = []
    list2 = []
    for i in range(1, number):
        if number % i == 0:
            list2.append(i)

    if sum(list2) == number:
        return "perfect"
    y = sum(list2)
    for j in range(1, y):
        if y % j == 0:
            list3.append(j)
    if sum(list3) == number:                #THIS SOLUTİON WİTH DEF FUNCTİON
        return "amicaple"
    else:
        return "neither"   

print(num_type(6))
print(num_type(2924)) 
print(num_type(5010))
  