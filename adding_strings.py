def add_str_nums(strnumber1, strnumber2):
    if strnumber1 == "" and strnumber2.isdigit():
        return strnumber2
    elif strnumber2 == "" and strnumber1.isdigit():
        return strnumber1
    
    
    if strnumber1.isdigit() and strnumber2.isdigit():
        strnumber1 = int(strnumber1)
        strnumber2 = int(strnumber2)
        total = strnumber1 + strnumber2
        return str(total)
    else:
        return "-1"
    
    

print(add_str_nums("1", ""))