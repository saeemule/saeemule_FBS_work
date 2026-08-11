set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}

missing_in_set2 = set1 - set2
missing_in_set1 = set2 - set1

print("Set1 =", set1)
print("Set2 =", set2)
print("Numbers in Set1 but missing in Set2 =", missing_in_set2)
print("Numbers in Set2 but missing in Set1 =", missing_in_set1)