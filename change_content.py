
import os
filepath = "files/"
path = os.listdir(filepath)
for content in path:
    print(content)
        
current = "sing"
new = "xxxx"
total = 0
for content in path:
    count = 0
   
    with open(filepath + content , "r", encoding="utf-8") as file:
        result = file.read()
        counter = result.count(current)

    result = result.replace(current, new)
    with open(filepath + content, "w", encoding="utf-8") as newfile:
        newfile.write(result)
        
    if counter:
        print(content, ":", counter, "changes")
        total += 1

print("Totally", total, "files changed") 