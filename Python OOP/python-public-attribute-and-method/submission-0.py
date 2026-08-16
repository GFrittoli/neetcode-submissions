class StoreItem:
    def __init__(self, name: str, price: int):
        self.name = name
        self.price = price

    def display_price(self) -> None:
        print(self.name)
        print(self.price)


chips = StoreItem("Chips", 1.99) # Don't modify this line

chips.display_price()

# TODO: Access the attributes of the chips object and display them


