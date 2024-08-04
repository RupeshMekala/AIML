max = int(input("Enter any number : "))

odd_numbers = []

for i in range(2, max):
    if i%2 != 0:
        odd_numbers.append(i)
print(odd_numbers)