# NAME : Adventure game

# THE IMPORTS THAT WE WILL NEED IT IN THIS PROJECT
import time
import random

# OUR VARIABLES
choose = ""
weapon = []
game_over = False
monsters = ["fairie", "butcher", "pirate", "dragon", "monster"]
monster = random.choice(monsters)


# This function is made to make sure that the input is right
def valid_input():
    global choose

    while True:
        choose = input("(Please enter 1 or 2.)\n")
        if choose == "1" or choose == "2":
            break


# This function is made to make time for each message
def print_pause(message):
    print(message)
    time.sleep(2)


# The intro for the game
def intro():
    print_pause("You find yourself standing in an open field,"
                " filled with grass and yellow wildflowers.")

    print_pause(f"Rumor has it that a wicked {monster}"
                " is somewhere around here, "
                "and has been terrifying the nearby village.")

    print_pause("In front of you is a house.")

    print_pause("To your right is a dark cave.")

    print_pause("In your hand you hold your trusty"
                " (but not very effective) dagger.\n")


def choices():
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.\n")
    print_pause("What would you like to do?")


def door():
    print_pause("You approach the door of the house.")

    print_pause(f"You are about to knock when "
                f"the door opens and out steps a wicked {monster}.")

    print_pause(f"Eep! This is the wicked {monster}'s house!")

    print_pause(f"The wicked {monster} attacks you!")

    print_pause("You feel a bit under-prepared for this,"
                " what with only having a tiny dagger.\n")

    print_pause("Would you like to (1) fight or (2) run away?\n")


def door2():
    print_pause("You approach the door of the house.")

    print_pause(f"You are about to knock when"
                f" the door opens and out steps a wicked {monster}.")

    print_pause(f"Eep! This is the wicked {monster}'s house!")

    print_pause(f"The wicked {monster} attacks you!")

    print_pause("Would you like to (1) fight or (2) run away?\n")


def with_sword():
    print_pause("As the gorgon moves to attack,"
                " you unsheath your new sword.")

    print_pause("The Sword of Ogoroth shines brightly in "
                "your hand as you brace yourself for the attack.")

    print_pause("But the gorgon takes one look at "
                "your shiny new toy and runs away!")

    print_pause("You have rid the town of the gorgon."
                " You are victorious!")


def without_sword():
    print_pause("You do your best...")
    print_pause(f"but your dagger is no match for the wicked {monster}.")
    print_pause("You have been defeated!")


def going_cave():
    print_pause("You peer cautiously into the cave.")

    print_pause("It turns out to be only a very small cave.")

    print_pause("Your eye catches a glint of "
                "metal behind a rock.")

    print_pause("You have found the magical Sword of Ogoroth!")

    print_pause("You discard your silly old dagger "
                "and take the sword with you.")

    print_pause("You walk back out to the field.\n")


def cave_again():
    print_pause("You peer cautiously into the cave.")

    print_pause("You've been here before, "
                "and gotten all the good stuff. "
                "It's just an empty cave now.")

    print_pause("You walk back out to the field.\n")


def run_cave():
    print_pause("You run back into the field. "
                "Luckily, you don't seem to have been followed.\n")


def play_again():
    global weapon

    print_pause("--- GAME OVER ---")

    while True:

        again = input("Would you like to play again? (y/n)\n").lower()
        if again == "y" or again == "n":
            break

    if again == "y":
        print_pause("Excellent! RESTARTING THE GAME ....")

        if "sword" in weapon:
            weapon.remove("sword")

        play_game()

    elif again == "n":
        print_pause("Thanks for playing! See you next time.")


def house():
    global game_over

    if "sword" in weapon:
        door2()

    else:
        door()

    valid_input()

    if choose == "1":

        if "sword" in weapon:
            with_sword()

            play_again()

        else:
            without_sword()

            play_again()

            game_over = True

    elif choose == "2":
        run_cave()
        field()


def field():
    get_order()


def cave():
    global weapon

    going_cave()

    weapon.append("sword")


def get_order():

    choices()

    valid_input()

    if choose == "1":
        house()

    elif choose == "2":
        if "sword" in weapon:
            cave_again()

            field()

        else:
            cave()

            field()


def play_game():
    intro()

    get_order()


play_game()
