
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
    "intro": "You see a shape rustling in the bushes",
    "adjective": "slimy",
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
fellwolf = {
    "name": "Fellwolf",
    "intro": "You hear a piercing howl and turn to face your foe",
    "adjective": "snarling",
    "attack_power": 4,
    "defense": 1,
    "weapon": "fangs",
    "hp": 8,
    "xp_drop": 2, #This is how much xp the bad guy gives when defeated
    "gold_drop": 1,
    "power": {
        "name": "Call For Help",
        "effect": "hp_up",
        "effect_impact": 10 }}

# Create a list to store enemies
enemies = [goblin,fellwolf]


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