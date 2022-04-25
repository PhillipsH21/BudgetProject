from Budget import Budget

#Example Budget class usage
test_budget = Budget("Test", 10)
print("Test budget category:", test_budget.get_category())
print("Test budget balance:", test_budget.get_balance())

test_budget.deposit(30)
print("Test budget balance after deposit:", test_budget.get_balance())

test_budget.withdraw(20)
print("Test budget balance after withdrawal:", test_budget.get_balance())

test_budget.set_balance(0)
test_budget.set_category("New category")
print("Test budget category:", test_budget.get_category())
print("Test budget balance:", test_budget.get_balance())



from Budget import Budget

categories = []
category = input("Please select a category or press Enter to quit: ")

while len(category) > 0:
    if category not in categories:
        categories.append(category)

        budget = float(input("Please enter your budget: "))
    else:

        final = Budget(category, budget)

        print("\nBudget category:", final.get_category())
        print(category, "budget balance:", final.get_balance())

        operation = input("Would you like to Deposit or Withdraw? ")

        if operation == "Deposit":
            dep_amount = float(input("Enter deposit amount: "))
            final.deposit(dep_amount)
            print("New", category, "budget balance:", final.get_balance())
            budget = final.get_balance()

        elif operation == "Withdraw":
            with_amount = float(input("Enter withdraw amount: "))
            final.withdraw(with_amount)
            print("New", category, "budget balance:", final.get_balance())
            budget = final.get_balance()

        category = input("\nPlease select a category or press Enter to quit: ")
else:
    quit
