str1 = "No I am not in a gang."
for i in str1:
    if not i.isalpha():
        str1 = str1.replace(i, " ")

str1 = str1.lower().split()
count = 0
for i in str1:
    if i[0] == i[-1] and len(i) > 1:                  #THIS SOLUTİON WİTH NORMAL METHODS
        count += 1
print(count)




def count_same_end(str1):
    for i in str1:
        if not i.isalpha():
            str1 = str1.replace(i, " ")

    str1 = str1.lower().split()
    count = 0
    for i in str1:
        if i[0] == i[-1] and len(i) > 1:                #THIS SOLUTİON WİTH DEF FUNCTİON
            count += 1
    return count 

print(count_same_end("No I am not in a gang."))