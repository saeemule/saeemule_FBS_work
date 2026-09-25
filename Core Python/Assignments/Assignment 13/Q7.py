student = {"name": "John", "age": 20, "grade": "A"}
key = input("Enter key to remove: ")

if key in student:
    del student[key]
    print(f"'{key}' removed successfully")
else:
    print(f"'{key}' not found in dictionary")

print("Dictionary after removal =", student)