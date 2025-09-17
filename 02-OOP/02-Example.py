# This example is based on one of the tasks of this course presented on the year 2021.
# Is not a complete implementation of the solution, but it illustrates the main concepts of OOP.

__author__ = "Calderon, 123456"

from typing import List

class Item:
    """
    Represents an item on the menu.
    """
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

class Table:
    """
    Represents a table in the restaurant and keeps track of the ordered items.
    """
    def __init__(self, number: int, seats: int):
        self.number = number
        self.seats = seats
        self.tab: List[Item] = []

    def calculate_total(self) -> float:
        """
        Calculate the total price of all items in the table.
        """
        total = 0.0
        for item in self.tab:
            total += item.price
        return total

    def add_item(self, item: Item):
        """
        Add an item to the table's order.
        """
        self.tab.append(item)

class VIPTable(Table):
    """
    Represents a VIP table in the restaurant that has an additional interest charge.
    """
    def __init__(self, number: int, seats: int, vip_interest: float):
        super().__init__(number, seats)
        self.vip_interest = vip_interest

    def calculate_total(self) -> float:
        """
        Calculate the total price of all items in the VIP table, including additional VIP services.
        """
        total = super().calculate_total()
        return total * self.vip_interest
    

if __name__ == "__main__":
    table1 = Table(1, 4)
    table2 = VIPTable(2, 4, 1.3)

    item1 = Item("Pizza", 12.99)
    item2 = Item("Pasta", 10.99)
    item3 = Item("Steak", 19.99)

    table1.add_item(item1)
    table1.add_item(item2)

    table2.add_item(item3)

    print(f"Total for Table 1: {table1.calculate_total():.2f} €")
    print(f"Total for VIP Table 2: {table2.calculate_total():.2f} €")