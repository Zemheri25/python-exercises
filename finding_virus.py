list1 = []
text = "PC Files: notvirus.exe, funnycat.gif".split(",")  
for i in text:
    list1.append(i) 
for j in list1:
    if "virus" in j:
        if "antivirus.exe"  not in j and "notvirus" not in j:
           list1.remove(j)
        else:
            None

a = ",".join(list1)
print(a)




list1 = []
def remove_virus(folders):
    for i in folders.split(","):
        list1.append(i)
    for j in list1:
      if "virus" in j:
        if "antivirus" not in j and "notvirus" not in j:         #THIS SOLUTİON WİTH DEFİNED FUNCTİON
           list1.remove(j)
        else:
            None
    a = ",".join(list1)
    return a

print(remove_virus("PC Files: antivirus.exe, cat.pdf, lethalmalware.exe, dangerousvirus.exe "))
