count = 0
number =input("Please enter your number ? ")
if number.isnumeric() and int(number) > 0:
    for i in number:
       i = int(i)
       count = count + i**len(number)
    if int(number) == count:
        print(f"{number} is an Armstrong number.")
    else:
        print(f"{number} is not an Armstrong number")  
else:
    print("It is an invalid entry.Don't use non-numeric,float or negative values!")


