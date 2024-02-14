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
    battle_tank = "battleVessel" + str(i+1)
    new_battle_tank = Tank(battle_tank)
    battle_tanks.append(new_battle_tank)

for battle_tank in battle_tanks:
    print(battle_tank)

# Randomly shuffle list of battle tanks
random.shuffle(battle_tanks)

# The tank at index 0 will first attack
attacking_tank = battle_tanks[0]
print("Attacking tank:", attacking_tank)

# Shuffling remaining items starting on index 1
remaining_tanks = battle_tanks[1:]
random.shuffle(remaining_tanks)

# Tank at index 0 receives the hit
hit_tank = remaining_tanks[0]
print("Receiving tank:", hit_tank)

# Attack and hit happens
attacking_tank.fires_at(hit_tank)
print(attacking_tank)
print(hit_tank)


# Should it blow?
if hit_tank.armor <= 0:
	hit_tank.explode()
	# Removes exploded battle tank
	battle_tanks.pop(battle_tanks.index(hit_tank))

# Current status
for battle_tank in battle_tanks:
	print(battle_tank)
