import game_data
# the entry point (the file we run python on for a test based RPG)

the_hero = game_data.the_hero
enemies = game_data.enemies
main_options = game_data.main_options

game_data.the_hero["name"] = input(("""What ho, Traveler! Welcome to the Drunken Dragon. What be thine name? """))
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