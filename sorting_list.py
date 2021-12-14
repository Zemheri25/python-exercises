list1 = [
  "John Locke",
  "Thomas Aquinas",
  "David Hume",
  "Rene Descartes"
]

value = input("Please enter your value 'ASC' or 'DESC' : ").upper()
dict1 = {}
for i in list1:
    i = i.split()
    dict1[i[0] +" "+ i[1]] = i[1]

if value == "ASC":
    for w in sorted(dict1.keys(), key=dict1.get, reverse=False):                 
        print(w)

else:    
    for w in sorted(dict1.keys(), key=dict1.get, reverse=True):
        print(w)
