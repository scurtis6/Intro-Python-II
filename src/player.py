from room import Room

# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_room: Room, inventory=None):
        self.name = name
        self.current_room = current_room
        if inventory is None:
            self.inventory = []
            # print('You have no inventory')
        else:
            self.inventory = inventory

    def __str__(self):
        return f'Player: {self.name}, Current Room: {self.current_room}'

    # picks up an item
    def takeItem(self, item):
        self.inventory.append(item)
        print(f'You have picked up a {item}')
    
    # drops off an item
    def dropItem(self, item):
        self.inventory.remove(item)
        print(f'You have dropped a {item}')
