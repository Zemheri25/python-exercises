list1 = []
text = "AB[3CD]"
for i in text:
    if i.isalpha() and not text[text.index(i)+1] == "]":
        list1.append(i)
    elif i.isnumeric():
        b = text.index("]")
        a = text[text.index(i)+1]
        list1.append(int(i) * text[text.index(a):b])
print(list1)







def space_message(text):
    list1 =[]
    for i in text:
        if i.isalpha() and not text[text.index(i)-1].isnumeric():
           list1.append(i)
        elif i.isnumeric():
           b = text.find("]")
           a = text[text.index(i)+1]
           list1.append(int(i) * text[a:b])
    return "".join(list1)

print(space_message("AB[3CD]"))
