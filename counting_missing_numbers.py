list1 = ["7", "3", "1", "9", "5"]
a = [i for i in list1 if i.isdigit()]
b = list(map(int, a))
c = [i for i in range(min(b), max(b))]          #THIS SOLUTİON WİTH NORMAL METHODS
d = len([i for i in c if i not in b])
print(d)
        

def count_missing_nums(list1):
    a = [i for i in list1 if i.isdigit()]
    b = list(map(int, a))
    c = [i for i in range(min(b), max(b))]          #THIS SOLUTİON WİTH DEF FUCNTİON
    d = len([i for i in c if i not in b])
    return d

print(count_missing_nums(["1", "5", "B", "9", "z"]))