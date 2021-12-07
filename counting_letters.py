
text = input("Please enter your text: ")
dict1 = {}
for i in text:
    dict1[i] = text.count(i)

print(dict1)