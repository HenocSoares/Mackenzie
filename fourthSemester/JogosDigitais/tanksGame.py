import pygame

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
