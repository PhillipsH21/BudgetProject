from Budget import Budget
from Transaction_History import Transactions, Node

categories = []
category = input("Please enter a category, type 'Transactions' to get full list of transactions, or press Enter to quit: ")
transaction_list = Transactions()

while len(category) > 0:
    if category not in categories and category != "Transactions":
        categories.append(category)

        budget = float(input("Please enter your budget: "))
    elif category == "Transactions":
        node = transaction_list.head
        while node is not None:
            print("Category: {}, Operation: {}, Amount: {}".format(node.category, node.action, node.amount))
            node = node.next
        category = input("Please enter a category, type 'Transactions' to get full list of transactions, or press Enter to quit: ")
    else:

        final = Budget(category, budget)

        print("\nBudget category:", final.get_category())
        print(category, "budget balance:", final.get_balance())

        operation = input("Would you like to Deposit, Withdraw, or Transfer? ")

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

        elif operation == "Transfer":
            receive_category = input("Enter the category you would like to transfer funds to: ")
            if receive_category not in categories:
                print("Category", receive_category, "does not exist.")
                break
            else:
                transfer_amount = float(input("Enter transfer amount: "))
                final.withdraw(transfer_amount)
                final = Budget(receive_category, budget)
                final.deposit(transfer_amount)
                print("New", receive_category, "budget balance:", final.get_balance())

            print("New", category, "budget balance:", final.get_balance())
            budget = final.get_balance()

        category = input("\nPlease enter a category, type 'Transactions' to get full list of transactions, or press Enter to quit: ")
else:
    quit
