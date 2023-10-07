# the entry point (the file we run python on for a test based RPG)


char_name = input(("What ho, Traveler! Welcome to the Drunken Dragon. What be thine name? "))

the_hero = {
    "name": char_name,
    "xp": 0, #use xp to deermine when to level up
    "gold": 5, #amount of money the player has to buy things
    "attack_power": 5,
    "defense": 2,
    "hp": 10,
    "weapon": "dull broadsword",
    "inventory": ["health_potion"]

}

# make a boolen flag that will control our main loop
GAME_ON = True

while GAME_ON:

    print(f"How can I be of service to ye, noble {char_name}?")
    print("1. Jobs around the village")
    print("2. Browse the Innkeep's wares")
    print("3. Hear the local gossip")
    print("4. Leave the Inn")
    action = input(" > ")
    if action == "4":
        print(f"Fare the well on thine travels, {the_hero['name']}")
        GAME_ON = False
