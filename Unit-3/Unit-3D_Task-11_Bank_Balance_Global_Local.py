balance = 1000
def deposit():
 global balance
 balance += 500
def display():
 balance = 200
 print("Local Balance:", balance)
deposit()
display()
print("Account Balance:", balance)