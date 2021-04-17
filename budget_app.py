class Budget:

    def __init__(self, category, amount):
        self.category = category
        self.amount = amount

    def deposit(self, amount):
        if amount <= 0:
            return "You can't deposit this amount"
        self.amount = self.amount + amount

    def withdraw(self, amount):
        if amount > self.amount:
            return "Insufficient Fund"
        self.amount = self.amount - amount

    def check_balance(self):
        return self.amount

    def make_transfer(self, amount_to_be_transferred, budget_obj):
        budget_obj.deposit(amount_to_be_transferred)


# --- TESTING THE METHODS ----
budget_object_1 = Budget("shoes",2000)
budget_object_2 = Budget("clothes", 3000)
budget_object_3 = Budget("hair", 1000)

# check balance method
print(budget_object_1.check_balance())

# deposit method
budget_object_1.deposit(3000)
print(budget_object_1.check_balance())

# make_transfer method
print(budget_object_2.check_balance())
budget_object_1.make_transfer(500, budget_object_2)
print(budget_object_2.check_balance())

# withdraw method
print(budget_object_3.check_balance())
budget_object_3.withdraw(200)
print(budget_object_3.check_balance())




