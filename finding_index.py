alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def alphabet_index(alphabet, text):
    text = input("Please enter your text : ")
    dict1 = {}
    for i in text:
        if i not in dict1: 
           dict1[i] = alphabet.index(i)

    a = max(dict1, key=dict1.get)
    return a

        
print(alphabet_index(alphabet, "omer"))  