def rectangle(l, b):
 area = l * b
 perimeter = 2 * (l + b)
 return area, perimeter
a, p = rectangle(10, 5)
print("Area:", a)
print("Perimeter:", p)