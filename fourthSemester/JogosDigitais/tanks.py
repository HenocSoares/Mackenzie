import random

class Tank(object):
    def __init__(self, name):
        self.name = name
        self.alive = True
        self.ammo = 5
        self.armor = 60

    def __str__(self):
        if self.alive:
            return "%s (%i armor, %i shells)" % (self.name, self.armor, self.ammo)
        else:
            return "%s (DEAD)" % self.name

    def fires_at(self, enemy):
        if self.ammo >= 1:
            self.ammo -= 1
            print(self.name, "fires on", enemy.name)
            enemy.hit()
        else:
            print(self.name, "has no shells!")

    def hit(self):
        self.armor -= 20
        print(self.name, "is hit")
        if self.armor <= 0:
            self.explode()

    def explode(self):
        self.alive = False
        print(self.name, "explodes!")

battle_tanks = []
for i in range(5):
    battle_tank = "battleVessel" + str(i + 1)
    new_battle_tank = Tank(battle_tank)
    battle_tanks.append(new_battle_tank)

for battle_tank in battle_tanks:
    print(battle_tank)

# Start and repeat (simulation) the draw process until we have a winner
while len(battle_tanks) > 1:
    # Randomly shuffle the list of battle tanks
    random.shuffle(battle_tanks)

    # Tank at index [0] will strike first
    attacking_tank = battle_tanks[0]
    print("Attacking tank:", attacking_tank)

    # Shuffling remaining items for first hit to happen from [1]
    remaining_tanks = battle_tanks[1:]
    random.shuffle(remaining_tanks)

    # Tank at [0] receives the hit
    hit_tank = remaining_tanks[0]
    print("Attacked tank:", hit_tank)

    # Attack plus hit happens
    attacking_tank.fires_at(hit_tank)
    print(attacking_tank)
    print(hit_tank)

    # Check if hit_tank should explode
    if hit_tank.armor <= 0:
        hit_tank.explode()
        # Removing exploded battle vessel via pop()
        battle_tanks.pop(battle_tanks.index(hit_tank))

    # Displays the updated state of the tanks after each round
    print("\nCurrent state:\n")
    for battle_tank in battle_tanks:
        print(battle_tank)

# Prints the winner vessel's name
print("The winner is:", battle_tanks[0])
