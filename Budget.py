class Budget():
    def __init__(self, category = "", initial_balance = 0):
        self.category = category
        self.balance = initial_balance

    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

    def get_category(self):
        return self.category

    def set_category(self, new_category):
        self.category = new_category

    def get_balance(self):
        return self.balance

    def set_balance(self, amount):
        self.balance = amount
