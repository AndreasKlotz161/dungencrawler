import enemy
import item

class room():

    def __init__(self, name, desc):
        self.doors = {"north": None, "east": None, "south": None, "west": None}
        self.name = name
        self.desc = "\033[47;30m "+desc+" \033[0m"
        self.enemies = []
        self.items = []

    def setDoors(self, north, east, south, west):
        self.doors["north"] = north
        self.doors["east"] = east
        self.doors["south"] = south
        self.doors["west"] = west

    def getName(self):
        return self.name

    def print(self):
        print(f"{self.desc}")
        if len(self.enemies) > 0:
            for enemy in self.enemies:
                print("There is a", enemy.getInfo())
        else:
            print("Everything is peaceful in here. RELAX!")

    def printItems(self):
        print("There are", end=" ")
        if len(self.items) > 0:
            print(f": ", end=" ")
            for elem in self.items:
                print(f"\033[31;43m{elem.getName()}\033[0m", end=" : ")
            print("")
        else:
            print("no items")

    def printDoors(self):    
        for key in self.doors.keys():
            if self.doors.get(key) != None:
                print(f"There is a way to \033[47;30m {self.doors.get(key).getName()} \033[0m in the {key}")

#    def addEnemy(self, name, hp, ap):
#        self.enemies.append(enemy.enemy(name, hp, ap))
    
    def addEnemy(self, name, hp, ap, items=None):
        newEnemy = enemy.enemy(name, hp, ap)
        if items != None:
            newEnemy.addItem(items)
        self.enemies.append(newEnemy)
        


    def getEnemyByName(self, name):
        if len(self.enemies) > 0:
            for enemy in self.enemies:
                if enemy.getName() == name:
                    return enemy
            print(f"There is no \033[31m{name}\033[0m in this room")
        else:
            print("No Enemies left.")
            
    def delEnemy(self):
        for enemy in self.enemies:
            if enemy.getHP() < 1:
                if len(enemy.items) > 0:
                    for elem in enemy.dropItems():
                        self.items.append(elem)

                print("You killed \033[23m" + self.enemies.pop(self.enemies.index(enemy)).getName() + "\033[0m")


    def putItem(self, name, type, value):
        self.items.append(item.item(name, type, value))

    def takeItemByName(self, itemName):
        for elem in self.items:
            if elem.getName() == itemName:
                return self.items.pop(self.items.index(elem))
        print(f"There is no {itemName}.")
        return None
        


