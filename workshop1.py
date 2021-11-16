input1 = int(input("Lütfen matematik notunuzu giriniz : "))
İnput2 = int(input("Lütfen ingilzice notunuzu giriniz : "))
input3 = int(input("Lütfen coğrafya notunuzu giriniz : "))
input4 = int(input("Lütfen kimya notunuzu giriniz : "))
input5 = int(input("Lütfen fizik notunuzu giriniz : "))
ortalama = (input1 + İnput2 + input3 + input4 + input5) / 5
if ortalama >= 90 and (input1 >= 85 and İnput2 >= 85 and input3 >= 85 and input4 >= 85 and input5 >= 85):
    print(f"Tebrikler Not ortalamanız = {ortalama} (AA) ve onur belgesine hak kazandınız!")
elif ortalama >= 90 and (input1 < 85 or İnput2 < 85 or input3 < 85 or input4 < 85 or input5 < 85):
    print(f"Tebrikler Not ortalamanız = {ortalama} (AA) ancak Onur belgesine hak kazanamadınız.")
elif 90 > ortalama >= 80 and (input1 >= 75 and İnput2 >= 75 and input3 >= 75 and input4 >= 75 and input5 >= 75):
    print(f"Tebrikler not ortalamanız = {ortalama} (AB) ve 1000 Euro hediye çeki kazandınız.")
elif 80 > ortalama >= 70 and (input1 >= 70 and İnput2 >= 70 and input3 >= 70 and input4 >= 70 and input5 >= 70):         #NOT ORTALAMA SORUSUDUR.
    print(f"Tebrikler not ortalamanız = {ortalama} (BB) ve 500 Euro hediye çeki kazandınız.")
elif 70 > ortalama >= 60:
    print(f"Not ortalamanız {ortalama} (BC)")
elif 60 > ortalama >= 50:
    print(f"Not ortalamanız = {ortalama} (CC)")
else:
    print(f"Not ortalamanız = {ortalama} (DD)")