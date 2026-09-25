words = ["eat", "tea", "tan", "ate", "nat", "bat"]

groups = {}
for word in words:
    key = "".join(sorted(word))
    if key in groups:
        groups[key].add(word)
    else:
        groups[key] = {word}

print("Anagram groups:")
for key, group in groups.items():
    print(group)