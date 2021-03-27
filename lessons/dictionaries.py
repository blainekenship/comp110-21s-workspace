"""Examples of dictionaries"""

#Establish a type with dict[key type, value type]
#Empty dictionary literal is {}
players: dict[str, int] = {}

# Insert a new key-value pair
# Refrence keys inside subscription notation, associated values are assigned
players["Brooks"] = 15
players["Love"] = 2
players["Bacot"] = 4
players["Bacot"] = players["Bacot"] + 1
print(players)


# for.. in loops will five you each key one by one
for player_name in players:
    print(f"{player_name} -> {players[player_name]}")

#You can have keys and values of any types. This is inverse of above, and a dict literal
jerseys: dict[int, str] = {15: "Brooks", 2: "Love", 5: "Bacot"}
jerseys[23] = "Jordan"
print(jerseys)

#The pop method allows you to remove a k/v pair by its key
popped_name: str = jerseys.pop(23)
print(popped_name)
print(jerseys)