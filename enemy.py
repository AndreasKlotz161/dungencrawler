import item

class enemy:

    def __init__(self, name, hp, ap):
        self.name = name
        self.hp = hp
        self.ap = ap
        self.items = []

    def dealDamage(self):
        return self.ap
    
    def takeDamage(self, damage):
        self.hp -= damage
        print(f"\033[32m{self.name}\033[0m took \033[31m{damage}\033[0m from player. It has now \033[33m{self.hp}\033[0m HP")

    def getInfo(self):
        return f"\033[32m{self.name}\033[0m. It has \033[33m{self.hp}\033[0m HP"
    
    def getName(self):
        return self.name
    
    def getHP(self):
        return self.hp
    
    def dropItems(self):
        if len(self.items) > 0:
            return self.items
    
    def addItem(self, newItem):
        if type(newItem) == list:
            for elem in newItem:
                self.items.append(elem)
        else:
            self.items.append(newItem)