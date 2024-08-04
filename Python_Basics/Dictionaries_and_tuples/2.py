
stocks = {"info": [600, 630, 620], "ril": [1430, 1490, 1567], "mtl": [234, 180, 160]}

user = input("What do you want to do 'print' or 'add' : ")
# A
if user == "print":
 for items in stocks:
    print(items, " ===> ", stocks[items])
# B
elif user == "add":
    stock = input("Enter the stock ticker :")
    price = int(input("Enter the price : "))
    check = stock in stocks
    if not check:
        stocks[stock] = price
        for items in stocks:
            print(items, " ===> ", stocks[items])

    elif check:
        stocks[stock].append(price)
        for items in stocks:
            print(items, " ===> ", stocks[items])








