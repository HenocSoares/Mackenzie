import pygame
import random

# O construtor que define os atributos da nossa classe (name, alive, ammo & armor)
class Tank (object):
    def __init__(self, name): # O construtor recebe como parâmetro o atributo nome
        self.name = name
        self.alive = True
        self.ammo = 5
        self.armor = 60
    
    def __str__(self):
        if self.alive:
            return "%s (%i armor, %i shells)" % (self.name, self.armor, self.ammo)
        else:
            return "%s (DEAD)" % self.name
    
    def fire_at(self, enemy): # Recebe por parâmetro o nome do inimigo a ser afetado
        if self.ammo >= 1:
            self.ammo -= 1
            print(self.name, "fires on", enemy.name)
            enemy.hit( )
        else:
            print(self.name, "has no shells!")

    def hit(self):
        self.armor -= 20
        print(self.name, "is hit")
        if self.armor <= 0:
            self.explode( )
    
    def explode(self):
        self.alive = False
        print(self.name, "explodes!")

t1 = Tank("Tanque1")
t2 = Tank("Tanque2")
t3 = Tank("Tanque3")
t4 = Tank("Tanque4")
t5 = Tank("Tanque5")

array = [t2, t2, t3, t4, t5]

while(len(array) != 1):
    num = random.randint(0, len(array)-1)
    num2 = random.randint(0, len(array)-1)
    while num2 == num:
        num2 = random.randint(0, len(array)-1)

    array[num].fire_at(array[num2])
    if(array[num2].alive != True):
        array.remove(array[num2])

print("\nO tanque", array[0].name, "venceu!")
