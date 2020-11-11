
import random

# Soldier

class Soldier:

    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
        pass
    
    def attack(self):
        return self.strength
        pass

    def receiveDamage(self,damage):
        self.health = self.health - damage
        pass

# This Function didnt work on BASH Terminal
# python -m unittest lab-data-vikings/1-testsSoldier.py

# Viking

class Viking(Soldier):

    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength
        pass
    
    def receiveDamage(self, damage):
        self.health = self.health - damage
        if self.health > 0:
            return f'{self.name} has received {damage} points of damage'
        else:
            return f'{self.name} has died in act of combat'
            pass

    def battleCry(self):
        return 'Odin Owns You All!'

# Saxon

class Saxon(Soldier):
    
    #def __init__(self, health, strength):
        #self.health = health
        #self.strength = strength
        #pass
        ### It doesnt affect the outputs if we dont add again the constructor function.
    
    def receiveDamage(self, damage):
        self.health = self.health - damage
        if self.health > 0:
            return f'A Saxon has received {damage} points of damage'
        else:
            return f'A Saxon has died in combat'
            pass
        pass

# War

class War:

    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []
        pass
    
    def addViking(self, viking):
        if isinstance(viking, Viking):
            self.vikingArmy.append(viking)
        else:
            raise ValueError("The function receives only objects from the Class Viking")
        pass

    def addSaxon(self, saxon):
        if isinstance(saxon, Saxon):
            self.saxonArmy.append(saxon)
        else:
            raise ValueError("The function receives only objects from the Class Saxon")
        pass
    
    def vikingAttack(self):
        saxon = random.choice(self.saxonArmy)
        viking_strength = random.choice(self.vikingArmy).strength
        attack_result = saxon.receiveDamage(damage=viking_strength)
        if saxon.health <= 0:
            self.saxonArmy.remove(saxon)
        return attack_result
        pass

    def saxonAttack(self):
        viking = random.choice(self.vikingArmy)
        saxon_strength = random.choice(self.saxonArmy).strength
        attack_result = viking.receiveDamage(damage=saxon_strength)
        if viking.health <= 0:
            self.vikingArmy.remove(viking)
        return attack_result
        pass
    
    def showStatus(self):
        if len(self.saxonArmy) == 0 and len(self.vikingArmy) > 0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0 and len(self.saxonArmy) > 0:
            return "Saxons have fought for their lives and survive another day..."
        elif len(self.saxonArmy) > 0 and len(self.vikingArmy) > 0:
            return "Vikings and Saxons are still in the thick of battle."
        else:
            return "The War's Status is Unknown ..."
        pass





