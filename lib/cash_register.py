#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []

    def add_item(self, title, price, quantity=1):
        self.total += price * quantity
        for _ in range(quantity):
            self.items.append(title)

    def apply_discount(self):
        if self.discount == 0:
            print("There is no discount to apply.")
            return
        discounted_amount = self.total * (1 - self.discount / 100)
        self.total = discounted_amount
        print(f"After the discount, the total comes to ${discounted_amount:.2f}.")
        return discounted_amount

    

