lines = ["the quick brown fox", "the lazy dog", "the fox jumps"]

all_words = []
for line in lines:
    all_words.extend(line.split())

unique_words = set(all_words)
print("Unique words =", unique_words)

frequency = {}
for word in unique_words:
    frequency[word] = all_words.count(word)

print("Word frequency =", frequency)