text = input("Enter a line: ")
with open("output.txt", "w") as file:
   file.write(text)
print("File written successfully.")