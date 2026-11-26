students = [
 {"name": "Pavan", "marks": 90},
 {"name": "Ravi", "marks": 75},
 {"name": "Kiran", "marks": 85}
]
ascending = sorted(students, key=lambda x: x["marks"])
descending = sorted(students, key=lambda x: x["marks"], reverse=True)
print("Ascending Order:")
print(ascending)
print("Descending Order:")
print(descending)
