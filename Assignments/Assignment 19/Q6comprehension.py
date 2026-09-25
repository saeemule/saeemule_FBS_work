text = input("Enter a sentence: ")
word_lengths = {word: len(word) for word in text.split()}
print("Word lengths:", word_lengths)