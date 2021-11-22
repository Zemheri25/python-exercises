count = 1
n = int(input("How many times 'ping' ?"))
text = n* "ping".split()
boolean = input("Please enter your bollean value : ")
if boolean == "True":
    while count < len(text) + 1:
        text.insert(count, "pong")
        count += 2
    print(text)

elif boolean == "False":                                 #NORMAL SOLUTİON
    while count < len(text):
        text.insert(count, "pong")
        count += 2
    print(text)

else:
    print("You got no acceptable value.")




def yerleştir(list1, bool):
    count = 1
    if bool == "True":
        while count < len(list1)+ 1:
            list1.insert(count, "pong")
            count += 2
        return list1
    elif bool == "False":
        while count < len(list1):                    #SOLUTİON WİTH FUNCTİON
            list1.insert(count, "pong")
            count += 2
        return list1
    else:
        return "You got no acceptable value"    