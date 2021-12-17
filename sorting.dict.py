dict2 = {}
list3 = []
list2 = []
list1 = [
  { "name": "a", "score": 100, "reputation": 20 },
  { "name": "b", "score": 90, "reputation": 40 },
  { "name": "c", "score": 115, "reputation": 30 },
]
for i in list1:
    count = 0
    list2 = [i["score"] + i["reputation"]*2 , i]
    list3.append(list2)

for i in list3:
    dict2[i[0]] = i[1]

import collections
od = collections.OrderedDict(sorted(dict2.items(), reverse=True))
for i in od.values():
    print(i)
