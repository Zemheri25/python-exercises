def summer(kelime):
    string1 = ""
    for i in range(len(kelime) -1):
        if kelime[i] != kelime[i+1]:
            string1 = string1 + kelime[i]
    string1 += kelime[-1]
    return string1

