import item

class player:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.ap = 20
        self.armorPoints = 0
        self.items = []
        self.weapon = None
        self.armor = None

    def takeDamage(self, damage, enemy):
        self.hp -= damage
        if self.hp > 0:
            print(f"You took \033[31m{damage}\033[0m damage from \033[36m{enemy}\033[0m and now have \033[32m{self.hp}\033[0m HP")
        else:
            print(f"You took \033[31m{damage}\033[0m damage from \033[36m{enemy}\033[0m and now are dead")

    def dealDamage(self):
        return self.ap
    
    def print(self):
        print(f"Status of {self.name}: HP: \033[32m{self.hp}\033[0m\t AP: \033[31m{self.ap}\033[0m\tArmor: \033[36m{self.armorPoints}\033[0m")
        if self.weapon != None:
            print(f"You yield a {self.weapon.getName()}.", end=" ")
        else:
            print(f"You have no weapon equipped.", end=" ")
        if self.armor != None:
            print(f"You're dressed in {self.armor.getName()}.")
        else:
            print("You're not dressed in armor.")

    def pickUpItem(self, itemPicked):
        self.items.append(itemPicked)
        print(f"You've picked up: {itemPicked.getName()}")

    def equipWeapon(self, weaponName):
        weapon = None
        for elem in self.items:
            if elem.getName() == weaponName:
                weapon = elem
                break
        if weapon != None:
            if weapon.getType() == "weapon":
                if self.weapon == None:
                    self.weapon = weapon
                    self.ap += self.weapon.getValue()
                    print(f"You equipped {weaponName}")
                else:
                    self.ap -= self.weapon.getValue()
                    self.items.append(self.weapon)
                    print(f"You put {self.weapon.getName()} in your bag and equipped {weaponName}")
                    self.weapon = weapon
                    self.ap += self.weapon.getValue()
                self.items.remove(weapon)
            else:
                print(f"You can't fight with a {weaponName}")
        else: 
            print("Your bag does not contain this item.")

    def equipArmor(self, armorName):
        armor = None
        for elem in self.items:
            if elem.getName() == armorName:
                armor = elem
                break
        if armor != None:
            if armor.getType() == "armor":
                if self.armor == None:
                    self.armor = armor
                    self.armorPoints = self.armor.getValue()
                    print(f"You equipped {armorName}")
                else:
                    self.items.append(self.armor)
                    print(f"You put {self.armor.getName()} in your bag and equipped {armorName}")
                    self.armor = armor
                    self.armorPoints = self.armor.getValue()
                self.items.remove(armor)
            else:
                print(f"You can't put on a {armorName}")
        else:
            print("You don't have that thingy")

    def consumeByName(self, consumableName):
        consumable = None
        for elem in self.items:
            if elem.getName() == consumableName:
                consumable = elem
                break
        if consumable != None:
            if consumable.getType() == "consumable":
                self.hp += consumable.getValue()
                self.items.remove(consumable)
                print(f"You indulged {consumableName} and gained {consumable.getValue()} HP")
            else:
                print(f"You can't consume {consumableName}")
        else:
            print(f"You don't have {consumableName}")

    def showInventory(self):
        if len(self.items) > 0:
            print("You have: |", end=" ")
            for elem in self.items:
                print(f"\033[34;43m{elem.getName()}\033[0m", end=" | ")
            print("")
        else:
            print("Your bag is empty.")
