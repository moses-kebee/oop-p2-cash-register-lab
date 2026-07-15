class CashRegister:
    def __init__(self, discount=0):
        # discount is validated through the property setter below
        self.discount = discount
        self.total = 0
        self.items = []
        self.previous_transactions = []

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, discount):
        # discount must be a whole number between 0 and 100 inclusive
        if isinstance(discount, int) and 0 <= discount <= 100:
            self._discount = discount
        else:
            print("Not valid discount")
            # keep a safe default so the object still works
            self._discount = getattr(self, "_discount", 0)

    def add_item(self, item, price, quantity=1):
        """Add an item to the register: updates total, items, and previous_transactions."""
        item_total = price * quantity
        self.total += item_total

        for _ in range(quantity):
            self.items.append(item)

        self.previous_transactions.append({
            "item": item,
            "price": price,
            "quantity": quantity
        })

    def apply_discount(self):
        """Apply the register's discount as a percentage off the total."""
        if self.discount > 0:
            self.total -= self.total * (self.discount / 100)
            print(f"After the discount, the total comes to ${self.total}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        """Undo the most recent transaction, adjusting total and items."""
        if self.previous_transactions:
            last_transaction = self.previous_transactions.pop()

            # correct the total
            self.total -= last_transaction["price"] * last_transaction["quantity"]

            # correct the items list
            for _ in range(last_transaction["quantity"]):
                self.items.remove(last_transaction["item"])
        else:
            print("There is no transaction to void.")