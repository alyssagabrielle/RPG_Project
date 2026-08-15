class character(object):
    def __init__(self,health,attackDamage):
        self.health = health
        self.attackDamage = attackDamage

    def takeDamage(self,amount):
        self.health = self.health - amount
        print(self.health)




