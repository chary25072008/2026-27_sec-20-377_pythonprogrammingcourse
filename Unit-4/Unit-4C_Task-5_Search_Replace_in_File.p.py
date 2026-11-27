old = input("Word to replace: ")
new = input("New word: ")
with open("sample.txt", "r") as file:
 text = file.read()
text = text.replace(old, new)
with open("sample.txt", "w") as file:
 file.write(text)
print("Replacement completed.")