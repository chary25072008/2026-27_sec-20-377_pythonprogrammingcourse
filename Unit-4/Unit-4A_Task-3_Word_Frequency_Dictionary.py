sentence = "python is easy python is useful"
words = sentence.split()
frequency = {}
for word in words:
 frequency[word] = frequency.get(word, 0) + 1
print("Word Frequency:")
print(frequency)
