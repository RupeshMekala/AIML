expense_list = [2340, 2500, 2100, 3100, 2980]
month_list = ["January", "February", "March", "April", "May"]

month_expense = int(input("Enter an amount : "))

month = -1
for x in range(len(expense_list)):
    if month_expense == expense_list[x]:
        print(f"{month_expense} were the expenses of {month_list[x]}")
        break

if month != -1:
    print(x + 1)

else:
    print("Expense not found")










