list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
union_list = list1[:]
for num in list2:
    if num not in union_list:
        union_list.append(num)
print("Union of two lists =", union_list)