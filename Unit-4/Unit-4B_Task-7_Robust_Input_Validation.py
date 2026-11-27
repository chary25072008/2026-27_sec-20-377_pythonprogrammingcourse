class InvalidMarksError(Exception):
   pass
try:
     marks = int(input("Enter marks: "))
     if marks < 0 or marks > 100:
      raise InvalidMarksError("Marks must be 0 to 100.")
      print("Pass" if marks >= 40 else "Fail")
except ValueError:
      print("Enter valid integer marks.")
except InvalidMarksError as error:
     print(error)
finally:
      print("Validation completed.")