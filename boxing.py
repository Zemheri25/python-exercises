
from random import choice

numbers = []
for i in range(101):
    numbers.append(i)

fighter1 = 0
fighter2 = 0
punch = 10

list1 = ["fighter1", "fighter2"]
c = choice(list1)
print(c)

fightend = False
if c == "fighter1":
    while fightend != True:
        fighter1 += punch
        print("fighter1 punch")
        a = choice(numbers)
        
        if a <= fighter1:
            fightend = True
            print("fighter1 wins")
        else:
            fighter2 += punch
            print("fighter2 punch")
            b = choice(numbers)
            
            if  b <= fighter2:
                fightend = True
                print("fighter2 wins")   

else:
    while fightend != True:
        fighter2 += punch
        print("fighter2 punch")
        b = choice(numbers)
        
        if b <= fighter2:
            fightend = True
            print("fighter2 wins")
        else:
            fighter1 += punch
            print("fighter2 punch")
            a = choice(numbers)
            
            if  a <= fighter1:
                fightend = True
                print("fighter1 wins") 





    




