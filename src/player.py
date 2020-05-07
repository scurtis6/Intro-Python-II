from room import Room

# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_room: Room, inventory=[]):
        self.name = name
        self.current_room = current_room
        self.inventory = inventory

    def __str__(self):
        return f'Player: {self.name}, Current Room: {self.current_room}'

    # picks up an item
    def takeItem(self, item):
        self.inventory.append(item)
    
    # drops off an item
    def dropItem(self, item):
        self.inventory.remove(item)
