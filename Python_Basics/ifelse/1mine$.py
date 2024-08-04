india = ["mumbai", "bengaluru", "chennai", "delhi"]
pakistan = ["lahore", "karachi", "islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

city1 = input("Enter first city name : ")
city2 = input("Enter second city name : ")

if city1 in india:
    if city2 in india:
        print("Both cities are in India")

elif city1 in pakistan:
    if city2 in pakistan:
        print("Both cities are in Pakistan")

elif city1 in bangladesh:
    if city2 in bangladesh:
        print("Both cities are in Bangladesh")

else:
    print("They don't belong to same country")

