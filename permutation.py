def permütasyon(n, r):
    counter1 = 1
    counter2= 1
    for i in range (1, n+1):
        counter1 = counter1*i
    for ii in range(1, n-r+1):
        counter2 = counter2*ii 
    return counter1 / counter2   

print(permütasyon(5, 4))