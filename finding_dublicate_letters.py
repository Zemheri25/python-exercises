def dublicate_word(text):
    list1 = []
    text= input("Please enter yuor text : ")
    text = text.split()
    for i in text:
        for j in range(len(i)-1):
            if i[j] == i[j+1]:
                list1.append(False)
            else:
                list1.append(True)
    return all(list1)

print(dublicate_word("text"))    
