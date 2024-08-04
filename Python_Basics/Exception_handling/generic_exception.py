x = input("Enter number 1 : ")
y = input("Enter number 2 : ")
try:
    z = x / int(y)  # we write the piece of code where we feel exception can occur in the try:

except Exception as e:

    print("Exception occured : ", e)
    z = None

print("Divisor is : ", z)
