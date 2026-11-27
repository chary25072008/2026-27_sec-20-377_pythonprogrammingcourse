try:
    number = int(input("Enter a number: "))
except ValueError:
     print("Invalid integer.")
else:
     print("Square:", number ** 2)
finally:
     print("Program finished.")