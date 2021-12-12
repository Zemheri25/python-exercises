list3 = []
list1 = [
  "artichokes ($1.99)",
  "rotiserrie chicken ($5.99)",
  "gum ($0.75)"
]
for i in list1:
    a = i.split()
    for j in a:
        if "$" in j:
            list3.append(j)    

print(list3)

a = "".join(list3)
for i in a:
    a = a.replace("(", "").replace(")", " ").replace("$", "")         #THIS SOLUTİON WİTH NORMAL METHODS
a = a.split()
a = map(float, a)
print(list(a))



list3 = []
def get_prices(list1):
    for i in list1:
        a = i.split()
        for j in a:
            if "$" in j:
                list3.append(j)

    a = "".join(list3)
    for i in a:
        a = a.replace("(", "").replace(")", " ").replace("$", "")     #THIS SOLUTİON WİTH DEF FUNCTİON
        a = a.split()
        a = map(float, a)
        return list(a)

print(get_prices([
  "artichokes ($1.99)",
  "rotiserrie chicken ($5.99)",
  "gum ($0.75)"
]))