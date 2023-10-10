
the_hero = {
    "name": "Incognito",
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