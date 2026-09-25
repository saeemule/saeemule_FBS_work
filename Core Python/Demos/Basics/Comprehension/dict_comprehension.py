#dict comprehension
li = [4,9,11,15]
dict = {
     x:x*x for x in li
       }
print(dict)