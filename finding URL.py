def domain_name(text):
    if text[9] != "w":
        a = text.find("/")
        b = text.find(".")
        x = text[a+2:b]
        print(x)
    else:
        first = text.find(".")
        second = text.rfind(".")

        total = text[first+1:second]
        print(total)

domain_name(input("Please etner your text : "))