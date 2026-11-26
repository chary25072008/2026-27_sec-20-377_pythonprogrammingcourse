student = {
 "name": "Pavan",
 "age": 18,
 "course": "Python"
}
print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())
print("Name:", student.get("name"))
student.update({"age": 19})
print("Updated:", student)
student.pop("course")
print("After Pop:", student)