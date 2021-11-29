list1 = []
def palindrome(text):
    for i in text:
        if i.isalpha():
            list1.append(i)
    a = "".join(list1).lower()
    b = a[::-1].lower()
    if a ==b:
        return True
    else:
        return False
print(palindrome("Go hang a salami, I'm a lasagna hog!"))