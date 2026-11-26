students = {
 1: {"name": "Pavan", "marks": 90},
 2: {"name": "Ravi", "marks": 85},
 3: {"name": "Kiran", "marks": 95}
}
for roll, details in students.items():
 print("Name:", details["name"])
 print("Marks:", details["marks"])