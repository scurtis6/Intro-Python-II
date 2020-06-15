# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description, items=None):
        self.name = name
        self.description = description
        if items is None:
            self.items = []
        else:
            self.items = items
        # AbbributeError: 'Room' object has no attribute 'n_to' fixed
        self.n_to = None
        self.e_to = None
        self.s_to = None
        self.w_to = None

    def __str__(self):
        return f'{self.name}, Description: {self.description}.'

    def add_Item(self, item):
        self.items.append(item)

    def remove_Item(self, item):
        self.items.remove(item)

    def displayItems(self):
        for item in self.items:
            print(item)
