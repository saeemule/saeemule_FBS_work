list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
intersection_list = []
for num in list1:
    if num in list2:
        intersection_list.append(num)
print("Intersection of two lists =", intersection_list)