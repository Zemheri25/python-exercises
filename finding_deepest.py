string1 = ([[[[[[[[[[1]]]]]]]]]])       
string1 = str(string1)
count  = 0

list1 = []

for i in string1:
    if i == "[":
        count += 1
        list1.append(count)
    elif i == "]":
        count -= 1
        list1.append(count)

print(max(list1))