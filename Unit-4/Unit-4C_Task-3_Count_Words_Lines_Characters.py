with open("sample.txt", "r") as file:
 text = file.read()
lines = text.splitlines()
words = text.split()
print("Lines:", len(lines))
print("Words:", len(words))
print("Characters:", len(text))