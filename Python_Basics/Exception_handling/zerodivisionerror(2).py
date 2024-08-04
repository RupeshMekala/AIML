x = input("Enter number 1 : ")
y = input("Enter number 2 : ")
try:
    z = x / int(y)
except ZeroDivisionError as e:
    print("Division by zero exception")
except TypeError as e:
    print('Type error exception')
    z = None
print("Divisor is : ", z)