list1 = [
  {
    "name": "Steve",
    "notes": [5, 5, 3, -1, 6]
  },
  {
    "name": "John",
    "notes": [3, 2, 5, 0, -3]
  }
]
dict1 = {}
list2 = []
for i in list1:
    a = i["notes"]
    for j in a:
        list2.append(j)

for i in list2:
    if 0 < i <= 5:
        dict1[i] = list2.count(i)

for i, j in dict1.items():
    print(i,":", j)