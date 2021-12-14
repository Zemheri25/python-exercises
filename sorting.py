def sort_array(list1):
    list2 = []
   
    while len(list1) != 0:
        minimum = min(list1)
        list2.append(minimum)
        list1.remove(minimum)
    return list2
print(sort_array([2, -5, 1, 4, 7, 8]))




def sort_array2(list1):
    list2 = []
    while len(list1) != 0:
        maximum = max(list1)
        list2.append(maximum)
        list1.remove(maximum)
    return list2

print(sort_array2([2, -5, 1, 4, 7, 8]))