student = {"name": "John", "age": 20, "grade": "A"}
key = input("Enter key to check: ")

if key in student:
    print(f"'{key}' exists in the dictionary")
else:
    print(f"'{key}' does NOT exist in the dictionary")