x = input("Enter number 1 : ")
y = input("Enter number 2 : ")
try:
    z = x / int(y)
except ZeroDivisionError as e:
    print("Division by zero exception")
    print("Division by zero exception")
except Exception as e:
    print('exception type : ', type(e).__name__)  # using __name__ will provide a concise answer,otherwise <class 'TypeError'>
    z = None
print("Divisor is : ", z)