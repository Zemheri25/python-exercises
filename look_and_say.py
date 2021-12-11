# number = int(input("Please enter your number : "))
# number = str(number)
# count1 = 0
# count2 = 1
# str1 = ""
# if len(number) % 2 == 0 and len(number) != 0:
#     for i in range(int(len(number) / 2)):
#         str1 += int(number[count1]) * number[count2]      #THIS SOLUTİON WİTH NORMAL METHODS
#         count1 += 2
#         count2 += 2
#     print(str1)
# else:
#     print("invalid")



def look_and_say(number):
    count1 = 0
    count2 = 1
    str1 = ""
    if len(number) % 2 == 0 and len(number) != 0:
        for i in range(int(len(number) / 2)):
            str1 += int(number[count1]) * number[count2]                                          #THIS SOLUTİON WİTH FUNCTİON 
            count1 += 2
            count2 += 2
        return str1
    else:
        return "invalid"

print(look_and_say("1213141516171819"))