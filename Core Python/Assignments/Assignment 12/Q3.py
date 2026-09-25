str1 = input("Enter first string: ").replace(" ", "").lower()
str2 = input("Enter second string: ").replace(" ", "").lower()

if len(str1) != len(str2):
    print("Not Anagrams")
else:
    list1 = list(str1)
    list2 = list(str2)
    list1.sort()
    list2.sort()
    if list1 == list2:
        print("The strings are Anagrams")
    else:
        print("The strings are NOT Anagrams")