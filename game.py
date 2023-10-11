# This is a core module that come wiht Python
from colorama import Fore, Back, Style
from time import sleep
import game_data
from battle_engine import battle_engine
# the entry point (the file we run python on for a test based RPG)

the_hero = game_data.the_hero
enemies = game_data.enemies
main_options = game_data.main_options

game_data.the_hero["name"] = input((Fore.BLUE +"""What ho, Traveler! Welcome to the Drunken Dragon. What be thine name? """))
print("...")
sleep(1.0)
print(f"Pleased to make yer acquaintance, {the_hero['name']}!")
print("...")
sleep(.75)
print("What Can I do fer ye this fine 'eve?")

#If the player decides to fight, this function will run
# make a boolen flag that will control our main loop
GAME_ON = True

while GAME_ON:
    for option in main_options:
        print(Fore.YELLOW+f"{option['input_key']}. {option['text']}")
        sleep(.25)
    action = input(" > ")
    if action == "4":
        print(f"Fare the well on thine travels, {the_hero['name']}")
        GAME_ON = False
    elif action == "1":
        battle_engine()