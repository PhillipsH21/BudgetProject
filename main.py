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


#Jack Stuff So Far
from Budget import Budget

def category_budget():
        categories = []
        category = input("Please select a category: ")

        while category not in categories:
            print("Category", category, "is not in category list. Would you like to create a new category for", category,
                  "?\nY or N")
            new_cat = input()

            if new_cat == "Y":
                categories.append(category)

                budget = float(input("Please enter your budget: "))

                Budget(category, budget)
                return

            else:
                break

category_budget()
