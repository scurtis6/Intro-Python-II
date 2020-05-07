class Item:
    def __init__(self, name, item_description):
        self.name = name
        self.item_description = item_description

    def __str__(self):
        return f'{self.name}\nMessage: {self.item_description}\n'