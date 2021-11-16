list1 = []
size = int(input("How many student will you enter : "))
count = 0
dict1 ={}
while count < size:
    student = input("Please enter your students with number : ").split()
    dict1[student[0]] = student[1:] 
    count += 1
name = input("Please enter name that you are looking for : ")
for i in dict1:
    if i == name:
        list1.append(dict1[i])
a = list(map(int, list1[0]))
print(sum(a) / len(a))



