from Budget import Budget
from TransactionHistory import Transactions, Node

categories = []
transaction_list = Transactions()

prompt_01 = """What would you like to do? (Please enter a number 1 - 6)
1: Display current categories and balances
2: Create a new budget category
3: Edit a budget category
4: Transfer funds
5: View transaction history
6: Quit
"""

prompt_02 = """What would you like to edit? (Please enter a number 1 - 3)
1: Edit category name
2: Edit category balance
3: Cancel
"""

prompt_03 = """How do you wish to transfer funds? (Please enter a number 1 - 4)
1: Deposit funds
2: Withdraw funds
3: Transfer funds between categories
4: Cancel
"""

def search_categories(category):
    index = 0
    while index < len(categories):
        if categories[index].get_category() == category:
            return index
        else:
            index += 1
    return -1

def record(list, action):
    list.append(Node(action))

while True:
    print()
    print(prompt_01)
    user_choice = input()
    print()

    if user_choice == "1":
        if len(categories) == 0:
            print("No categories have been created yet.")
        else:
            for item in categories:
                print("Category: {}\tBalance: ${}".format(item.get_category(), item.get_balance()))

    elif user_choice == "2":
        new_category = input("Please enter a new budget category: ")
        new_category_index = search_categories(new_category)

        if new_category_index == -1:
            new_balance = input("Please enter an initial balance for \"{}\": ".format(new_category))

            try:
                new_balance = int(new_balance)
                if new_category_index == -1:
                    categories.append(Budget(new_category, new_balance))
                    record(transaction_list, "Created new category \"{}\" with balance of ${}".format(new_category, new_balance))
                else:
                    print("This category already exists.")
            except ValueError:
                print("Invalid balance")
        else:
            print("Category already exists.")

    elif user_choice == "3":
        edit_category = input("Please enter the budget category that you wish to edit: ")
        edit_category_index = search_categories(edit_category)

        if edit_category_index == -1:
            print("Category not found.")
        else:
            edit_choice = input(prompt_02)
            if edit_choice == "1":
                edit_category = input("Please enter a new category name: ")
                edit_category_index = search_categories(edit_category)

                if edit_category_index == -1:
                    old_category = categories[edit_category_index].get_category()
                    categories[edit_category_index].set_category(edit_category)
                    record(transaction_list, "Changed name of category \"{}\" to \"{}\"".format(old_category, edit_category))
                else:
                    print("\"{}\" is used by an existing category".format(edit_category))
            elif edit_choice == "2":
                edit_balance = input("Please enter a new balance for \"{}\": ".format(categories[edit_category_index].get_category()))

                try:
                    edit_balance = int(edit_balance)
                    old_balance = categories[edit_category_index].get_balance()
                    categories[edit_category_index].set_balance(edit_balance)
                    record(transaction_list, "Changed balance of \"{}\" from ${} to ${}".format(edit_category, old_balance, edit_balance))
                except ValueError:
                    print("Invalid balance")

            elif edit_choice == "3":
                print("Nothing was changed")
            else:
                print("Invalid input")

    elif user_choice == "4":
        transfer_choice = input(prompt_03)

        if transfer_choice == "1":
            deposit_category = input("Please enter the category you would like to deposit funds to: ")
            deposit_category_index = search_categories(deposit_category)

            if deposit_category_index == -1:
                print("Category not found.")
            else:
                deposit_amount = input("Please enter the amount that you would like to deposit to \"{}\": ".format(deposit_category))

                try:
                    deposit_amount = int(deposit_amount)
                    categories[deposit_category_index].deposit(deposit_amount)
                    record(transaction_list, "Deposited ${} to \"{}\"".format(deposit_amount, deposit_category))
                except ValueError:
                    print("Invalid amount")

        elif transfer_choice == "2":
            withdraw_category = input("Please enter the category you would like to withdraw funds from: ")
            withdraw_category_index = search_categories(withdraw_category)

            if withdraw_category_index == -1:
                print("Category not found.")
            else:
                withdraw_amount = input("Please enter the amount that you would like to withdraw from \"{}\": ".format(withdraw_category))

                try:
                    withdraw_amount = int(withdraw_amount)
                    if withdraw_amount > categories[withdraw_category_index].get_balance():
                        print("Cannot complete transfer; insufficient funds")
                    else:
                        categories[withdraw_category_index].withdraw(withdraw_amount)
                        record(transaction_list, "Withdrew ${} from \"{}\"".format(withdraw_amount, withdraw_category))
                except:
                    print("Invalid amount")

        elif transfer_choice == "3":
            from_category = input("Please enter the category you would like to transfer funds from: ")
            from_category_index = search_categories(from_category)

            if from_category_index == -1:
                print("Category not found")

            to_category = input("Please enter the category you would like to transfer funds to: ")
            to_category_index = search_categories(to_category)

            if to_category_index == -1:
                print("Category not found")

            if (from_category_index == -1 or to_category_index == -1):
                print("Cannot complete transfer; one or more categories were not found.")
            else:
                print("Category: {}\tBalance: ${}".format(categories[from_category_index].get_category(), categories[from_category_index].get_balance()))
                print("Category: {}\tBalance: ${}".format(categories[to_category_index].get_category(), categories[to_category_index].get_balance()))

                transfer_amount = input("Please enter the amount you would like to transfer from \"{}\" to \"{}\": ".format(from_category, to_category))

                try:
                    transfer_amount = int(transfer_amount)
                    if transfer_amount > categories[from_category_index].get_balance():
                        print("Cannot complete transfer; amount exceeds balance of \"{}\".".format(from_category))
                    else:
                        categories[to_category_index].deposit(transfer_amount)
                        categories[from_category_index].withdraw(transfer_amount)
                        record(transaction_list, "Transferred ${} from \"{}\" to \"{}\"".format(transfer_amount, from_category, to_category))
                except ValueError:
                    print("Invalid amount")

        elif transfer_choice == "4":
            pass
        else:
            print("Invalid input")

    elif user_choice == "5":
        operation = transaction_list.head
        while operation != None:
            print(operation.action)
            operation = operation.next

    elif user_choice == "6":
        break

    else:
        print("Invalid input.")