def wrap_around(string1, number1):
    string1 = input("Please enter your string1 : ")
    number1 = int(input("Please enter your number1 : "))
    if number1 > 0:
        return string1[number1-1:] + string1[:number1]
    else:
        return string1[-1:number1-1:-1][::-1] + string1[:number1]

print(wrap_around("string1", "number1"))
