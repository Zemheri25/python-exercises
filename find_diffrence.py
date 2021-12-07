string1 = input("Please enter your string1 : ")
string2 = input("Please enter your string2 : ")
list1 = []
for i in string1:
    if i not in string2:
        list1.append(i)                                            #THIS SOLUTİON WİTH NORMAL METHODS

for i in string2:
    if i not in string1:
        list1.append(i)
print(list1)


def find_the_difference(string1, string2):
    list1 = []
    string1 = input("Please enter your string1 : ")
    string2 = input("Please enter your string2 : ")
    for i in string1:
        if i not in string2:
            list1.append(i)                                         #THIS SOLUTİON WİTH FUNCTİON
    for i in string2:
        if i not in string1:
            list1.append(i)
    return list1

print(find_the_difference("string1", "string2"))