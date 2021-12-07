my_karışık = ("Hello", "Bye", True, True, False, {"1": "One", "2": "Two"}, [1, 3], {"Brayan": 18}, 25, 23)
count_int = 0
count_str = 0
count_bool = 0
count_tuple = 0
count_dictionary = 0
count_list = 0
for i in my_karışık:
    if type(i) == int:
        count_int += 1                                                        #THIS SOLUTİON WİTH NORMAL METHODS
    elif type(i) == str:
        count_str += 1
    elif type(i) == dict:
        count_dictionary += 1
    elif type(i) == bool:
        count_bool += 1
    elif type(i) == tuple:
        count_tuple += 1
    elif type(i) == list:
        count_list += 1

list1 = [count_int, count_str, count_bool, count_list, count_tuple, count_dictionary]
print(list1)


def count_datatypes(values):
    count_int = 0
    count_str = 0
    count_bool = 0
    count_tuple = 0
    count_dictionary = 0
    count_list = 0
    for i in values:
        if type(i) == int:
            count_int += 1
        elif type(i) == str:
            count_str += 1
        elif type(i) == dict:                                                     #THİS SOLUTİON WİTH FUNCTİON
            count_dictionary += 1
        elif type(i) == bool:
            count_bool += 1
        elif type(i) == tuple:
            count_tuple += 1
        elif type(i) == list:
            count_list += 1
    list1 = [count_int, count_str, count_bool, count_list, count_tuple, count_dictionary]
    return list1

print(count_datatypes(([10, 20], ("t", "Ok"), 2, 3, 1)))
