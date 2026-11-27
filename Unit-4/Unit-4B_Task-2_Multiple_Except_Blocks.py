values = [10, 20, 30]
try:
    index = int(input("Enter index: "))
    print(values[index])
except ValueError:
     print("Enter an integer.")
except IndexError:
    print("Index out of range.")