from room import Room
from player import Player
import textwrap

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player('Sierra', room['outside'])
# print(player)

# Write a loop that:
while True:
    current_room = player.current_room
    print()

    # * Prints the current room name
    print(f'Current Room: {player.current_room.name}\n')

    # * Prints the current description (the textwrap module might be useful here).
    wrapper = textwrap.TextWrapper(width=45)

    description_list = wrapper.wrap(text=player.current_room.description)
    for words in description_list:
        print(words)

    # * Waits for user input and decides what to do.
    user_input = input('\nWhere do you want to go? Select n, e, s, w or q to quit: ')

    try:
        # If the user enters a cardinal direction, attempt to move to the room there.
        if user_input == 'n':

            if player.current_room.n_to is not None:
                player.current_room = current_room.n_to
                print('\nYou picked north!')
            else:
                # throws an error message
                print('\nTry again. There is no room that way!')
                
        elif user_input == 'e':

            if player.current_room.e_to is not None:
                player.current_room = current_room.e_to
                print('\nYou picked east!')
            else:
                # throws an error message
                print('\nTry again. There is no room that way!')

        elif user_input == 's':

            if player.current_room.s_to is not None:
                player.current_room = current_room.s_to
                print('\nYou picked south!')
            else:
                # throws an error message
                print('\nTry again. There is no room that way!')

        elif user_input == 'w':

            if player.current_room.w_to is not None:
                player.current_room = current_room.w_to
                print('\nYou picked west!')
            else:
                # throws an error message
                print('\nTry again. There is no room that way!')

        else:
            # Print an error message if the movement isn't allowed.
            print('\nPlease Enter: n, e, s, w or q')

    except AttributeError:
        pass

# If the user enters "q", quit the game.
    if user_input == 'q':
        print('\nThanks for playing with us!\n')
        break