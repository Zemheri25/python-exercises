dict1 = {}
list1 = ["99a", "78b", "c2345", "11d"]
for i in list1:
    for j in i:
        if j.isalpha():
            dict1[i] = ord(j)

list2 = []
sorted_x = sorted(dict1.items(), key=lambda kv: kv[1])          #THIS SOLUTIİN WİTH NORMAL METHODS
for i in sorted_x:
    list2.append(i[0])

print(list2)


def sort_by_letter(list):
    dict1 = {}
    for i in list:
        for j in i:
            if j.isalpha():
                dict1[i] = ord(j)
    list2 = []
    sorted_x = sorted(dict1.items(), key=lambda kv: kv[1])        #THIS SOLUTİON WİTH FUNCTION
    for i in sorted_x:
        list2.append(i[0])
    
    return list2

print(sort_by_letter(["99a", "78b", "c2345", "11d"]))