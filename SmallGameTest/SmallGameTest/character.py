class character(object):
    def __init__(self,health,name):
        self.health = health
        self.name = name
        self.equippedWeapon = None

    def takeDamage(self,amount):
        self.health = self.health - amount

    def equip(self,weapon):
        self.equippedWeapon = weapon





