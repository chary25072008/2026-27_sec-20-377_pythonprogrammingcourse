a = [1, 2, 3, 4, 5]
square = list(map(lambda x: x*x, a))
even = list(filter(lambda x: x % 2 == 0, a))
total = list(lambda x, y: x+y, a)
print("Squares:", square)
print("Even:", even)
print("Sum:", total)