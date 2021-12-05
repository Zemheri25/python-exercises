
list1 = []
size = int(input("How many value are you gonna enter : "))
for j in range(size):
    value = input("Please enter your value")
    list1.append(value)
build = input("Please enter your build : ").lower()       
list2 = []           
if build == "odd":
    count = 0 
    for i in range(round(len(list1) / 2 + 0.1) ):
       list2.append(list1[count])
       count += 2

elif build == "even":
    count = 1
    for i in range(round(len(list1) / 2 ) ):
        list2.append(list1[count])
        count += 2


print(list1)
print(list2)
    