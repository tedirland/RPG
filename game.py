# This is a core module that come wiht Python
import random
import game_data
# the entry point (the file we run python on for a test based RPG)

the_hero = game_data.the_hero
enemies = game_data.enemies
main_options = game_data.main_options

game_data.the_hero["name"] = input(("""What ho, Traveler! Welcome to the Drunken Dragon. What be thine name? """))
#If the player decides to fight, this function will run
def fight() -> None:

    random_index = random.randint(0,len(enemies)-1)
    print(random_index)
    enemy_encountered = enemies[random_index]
    in_fight = True #boolean that keeps us in the fight loop
    print(f"{enemy_encountered['intro']}")
    print(f"A {enemy_encountered['adjective']} {enemy_encountered['name']} appears...")
    while(in_fight):
        print(f"You have {the_hero['hp']} health points remaining \n The {enemy_encountered['name']} has {enemy_encountered['hp']}")
        print(f"1. Attack using {the_hero['weapon']}")
        health_potion_count = the_hero['inventory'].count('health_potion')
        print(f"2. Drink a health potion. ({health_potion_count} in your satchel)")
        print("3. Defend")
        print("4. Do a little dance")
        print("5. Run away")
        battle_action = input("What would you like to do? >")
    # Hero's turn
        if battle_action == "1":
            # user has chosen to attach
            # take the hero's attack power - monster'd defense
            # reduce the monster's hp by this calcuation
            damage_dealt = the_hero['attack_power'] - enemy_encountered['defense']
            print(f"You strike the {enemy_encountered['name']} for {damage_dealt} damage")
            enemy_encountered['hp'] -= damage_dealt
            if enemy_encountered['hp'] > 0:
                print("Your foe staggers but remains in the fight")
            else:
                print("Your blade crunches through flesh and bone. The beast lies still and does not rise")
                the_hero['xp'] += enemy_encountered['xp_drop']
                the_hero['gold'] += enemy_encountered['gold_drop']
                print(f"You earn {enemy_encountered['xp_drop']} xp and collect {enemy_encountered['gold_drop']} gold")
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