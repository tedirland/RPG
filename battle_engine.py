import random
from colorama import Fore, Back, Style
from game_data import enemies, the_hero
from quests import quests

enemies = enemies
the_hero = the_hero

def battle_engine():
    random_index = random.randint(0,len(enemies)-1)
    # we need to use the copy() method so we don't change the original
    enemy_encountered = enemies[random_index].copy()
    in_fight = True #boolean that keeps us in the fight loop
    print(f"{enemy_encountered['intro']}")
    print(f"A {enemy_encountered['adjective']} {enemy_encountered['name']} appears...")
    while in_fight:
        
        enemy_attack_modifier = 1
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
            print(Fore.GREEN + f"You strike the {enemy_encountered['name']} for {damage_dealt} damage")
            enemy_encountered['hp'] -= damage_dealt
            # Enemy's turn, if alive
            if enemy_encountered['hp'] > 0:
                print("Your foe staggers but remains in the fight")
                damage_dealt = (enemy_encountered['attack_power'] * enemy_attack_modifier) - the_hero['defense']
                print(f"The {enemy_encountered['name']} strikes for {damage_dealt} damage")
                the_hero['hp'] -= damage_dealt

            else:
                print("Your blade crunches through flesh and bone. The beast lies still and does not rise")
                the_hero['xp'] += enemy_encountered['xp_drop']
                the_hero['gold'] += enemy_encountered['gold_drop']
                print(f"You earn {enemy_encountered['xp_drop']} experience and collect {enemy_encountered['gold_drop']} gold")
                in_fight = False
        elif battle_action == "2":
            # Drink a potion
            if health_potion_count > 0:
                the_hero['inventory'].remove("health_potion")
                the_hero['hp'] = the_hero['max_hp']
                print("You take a health potion from your satchel and drink it greedily, restoring your lost hp")
            else:
                print("You reach into your satched for a potion. Your fingers grasp air")
                print(f"The {enemy_encountered['name']} takes advantage of your distraction")
        elif battle_action == "5":
            print("You flee successfully!")
            in_fight = False
