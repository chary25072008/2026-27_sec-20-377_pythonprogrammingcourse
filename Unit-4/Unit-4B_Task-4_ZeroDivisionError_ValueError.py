try:
    a = float(input("Numerator: "))
    b = float(input("Denominator: "))
    print("Result:", a / b)
except ZeroDivisionError:
     print("Denominator cannot be zero.")
except ValueError:
     print("Enter valid numbers.")