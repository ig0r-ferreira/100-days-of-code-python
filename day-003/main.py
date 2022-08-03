print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

game_over_msg = "Game Over."

choice = input(
    'You\'re at a crossroad. Where do you want to go? Type "left" or "right"\n' \
    '=> '
).lower()


if choice == "left":  
    choice = input(
        'You\'ve come to a lake. There is an island in the middle of the lake. ' \
        'Type "wait" to wait for a boat. Type "swim" to swim across.\n' \
        '=> '
    ).lower()
    
    if choice == "swim":
        choice = input(
            "You arrive at the island unharmed. There is a house with 3 doors. " \
            "One red, one yellow and one blue. Which colour do you choose?\n" \
            "=> "
        ).lower()

        if choice == "blue":
            print("You exploded! Boommm!", game_over_msg)
        elif choice == "yellow":
            print("You walked into a room full of lions!", game_over_msg)
        elif choice == "red":
            print("You found the treasure! You Win!")
        else:
            print("You failed to choose a door and the floor beneath you opened up!", game_over_msg)
    else:
        print("You waited too long and the crocodiles entered the water to attack you!", game_over_msg)
else:
    print("You were abducted by aliens!", game_over_msg)