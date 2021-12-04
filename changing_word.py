vowels = "aeıouu"
string1 = ""
alp = "abcdefghıijklmnoprstuvwxyz"
text = input("Please enter your text  : ")
for i in text:
    if i.isalpha():   
       if i not in vowels:
          string1 += alp[alp.index(i) + 1]
       
       else:
           string1 += i.upper()
    else:
        string1 += i

print(string1)
