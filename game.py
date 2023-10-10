import random as r
import time as t
# the entry point (the file we run python on for a test based RPG)


char_name = input(("What ho, Traveler! Welcome to the Drunken Dragon. What be thine name? "))

the_hero = {
    "name": char_name,
    "xp": 0, #use xp to determine when to level up
    "gold": 5, #amount of money the player has to buy things
    "attack_power": 5,
    "defense": 2,
    "hp": 10,
    "weapon": "dull broadsword",
    "inventory": ["health_potion"]

}

goblin = {
    "name": "Hill Goblin",
    "features": "slimy nose",
    "attack_power": 3,
    "defense": 0,
    "weapon": "rusty dagger",
    "hp": 6,
    "xp_drop": 2, #This is how much xp the bad guy gives when defeated
    "gold_drop": 1,
    "power": {
        "name": "Berzerk",
        "effect": "attack_up",
        "effect_impact": 5 }}

# Create a list to store enemies
enemies = []
enemies.append(goblin)

main_options = [
   { "text": "Jobs around the village",
    "input_key": "1"},
   { "text": "Browse the Innkeep's wares",
    "input_key": "2"},
   { "text": "Do a dance",
    "input_key": "3"},
   { "text": "Leave the inn (exit)",
    "input_key": "4"},
]

#If the player decides to fight, this function will run
def fight():
    enemy_encountered = enemies[0]
    in_fight = True #boolean that keeps us in the fight loop
    while(in_fight):
        print(f"A slimy {enemy_encountered['name']} appears...")
        battle_action = input("What would you like to do? >")
        in_fight = False


# make a boolen flag that will control our main loop
GAME_ON = True

while GAME_ON:
    for option in main_options:
        print(f"{option['input_key']}. {option['text']}")
    action = input(" > ")
    if action == "4":
        print(f"Fare the well on thine travels, {the_hero['name']}")
        GAME_ON = False
    elif action == "1":
        fight()
       




