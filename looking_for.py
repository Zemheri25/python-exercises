
list1 = []
sentences = "I have a cat. I have a mat. Things are going swell.".split(".")
word = "Things"
for i in sentences:
    if word in i:
        list1.append(i)

print(list1[0]+".")



def sentences_Searcher(text, word):
    list1 = []
    text = input("Please enter your text : ").split(".")
    word = input("Please enter yuor word : ")
    for i in text:
        if word in i:
            list1.append(i)
    return list1[0]+"."

print(sentences_Searcher("text", "word"))