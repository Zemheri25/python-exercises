from random import choice
list1 = ["taş", "kağıt", "makas"]
while True:
    seçim = input("Please enter your taş,kağıt,makas : ")
    a = choice(list1)
    
    if a == "taş" and seçim == "kağıt":
        print(f"{a},{seçim} sen kaznadın!")
        break
    elif a == "kağıt" and seçim == "makas":
        print(f"{a}, {seçim} sen kazandın")
        break
    elif a == "makas" and seçim == "taş":
        print(f"{a},{seçim} sen kazandın")
        break
    elif a == "taş"and seçim == "makas":
        print(f"{a}, {seçim}bilgisayar kazandı.")
        break
    elif a == "makas"and seçim == "kağıt":
        print(f"{a}, {seçim}bilgisayar kazandı.")
        break
    elif a == "kağıt"and seçim == "taş":
        print(f"{a}, {seçim}bilgisayar kazandı.")
        break
    else:
        print(f"{a}, {seçim} BERABERE")