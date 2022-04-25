from Budget import Budget
#O'Neal 
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


#Jack Stuff So Far
from Budget import Budget
from Transaction_History import Transactions, Node

categories = []
category = input("Please enter a category, type 'transactions' to get full list of transactions, or press Enter to quit:")
transaction_list = Transactions()

while len(category) > 0:
    if category not in categories and category is not "transactions":
        categories.append(category)

        budget = float(input("Please enter your budget: "))
    elif category is "transactions":
        node = transaction_list.head
        while node is not None:
            print("Category: {}, Operation: {}, Amount: {}".format(node.category, node.action, node.amount))
            node = node.next
        print()
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
            new_node = Node(category, operation, dep_amount)
            transaction_list.append(new_node)

                        
        elif operation == "Withdraw":
            with_amount = float(input("Enter withdraw amount: "))
            final.withdraw(with_amount)
            print("New", category, "budget balance:", final.get_balance())
            budget = final.get_balance()
            new_node = Node(category, operation, with_amount)
            transaction_list.append(new_node)

        category = input("\nPlease select a category or press Enter to quit: ")
else:
    quit
