import player
import room
import item

import os
import time


player1 = player.player(input("Enter your name troubleseeker: "))

#first define the rooms
entrance = room.room("entrance", "Nothing special Room")
chamber = room.room("chamber", "You are in a messy mossy chamber")
treasureRoom = room.room("treasure room", "You are in a room with a lot of valueable stuff lying all over the place")

#add enenmies to the rooms
entrance.addEnemy("bug", 40, 10)
treasureRoom.addEnemy("bug", 40, 10, [item.item("potion", "consumable", 30), item.item("full iron", "armor", 12)])

#add items to the rooms
treasureRoom.putItem("sword", "weapon", 20)

#set Dooors for all rooms
entrance.setDoors(None, chamber, None, treasureRoom)
chamber.setDoors(None, None,None, entrance)
treasureRoom.setDoors(None, entrance, None, None)
activeRoom = entrance
#-----------RUN-----------

while(player1.hp > 0):
    os.system('cls')
    
    player1.print()
    activeRoom.print()
    action = input("What do you want to do? A.ttack M.ove S.earch I.nventory: ").strip().upper()
    if action == "A":
        att = input("Enter\033[32m enemyname\033[0m you wanna attack: ")
        if activeRoom.getEnemyByName(att):
            activeRoom.getEnemyByName(att).takeDamage(player1.dealDamage())
            activeRoom.delEnemy()
        else:
            print(f"There is no {att} you dumbass.")
    elif action == "M":
        activeRoom.printDoors()
        direction = input("Which direction (N/E/S/W)? ").strip().upper()
        if direction == "N" and activeRoom.doors["north"] != None:
            activeRoom = activeRoom.doors["north"]
            continue
        elif direction == "E" and activeRoom.doors["east"] != None:
            activeRoom = activeRoom.doors["east"]
            continue
        elif direction == "S" and activeRoom.doors["south"] != None:
            activeRoom = activeRoom.doors["south"]
            continue
        elif direction == "W" and activeRoom.doors["west"] != None:
            activeRoom = activeRoom.doors["west"]
            continue
        else:
            print("You shall not pass!")
    elif action == "S":
        activeRoom.printItems()
        if activeRoom.items:
            searchAction = input("Do you want to pick any? Y/N/A.ll: ").strip().upper()
            if searchAction == "Y":
                newItem = activeRoom.takeItemByName(input("Enter the name of the item: "))
                if newItem:
                    player1.pickUpItem(newItem)
            elif searchAction == "A":                
                while len(activeRoom.items) > 0:
                    player1.items.append(activeRoom.items.pop())
    elif action == "I":
        if player1.items:
            player1.showInventory()
            itemAction = input("Do you want to equip A.rmor W.eapon or C.onsume something? ").strip().upper()
            if itemAction == "A":
                player1.equipArmor(input("Enter the name of the armor to equip: "))
            elif itemAction == "W":
                player1.equipWeapon(input("Enter the name of the weapon to equip: "))
            elif itemAction == "C":
                player1.consumeByName(input("Enter the name of the item to consume: "))
        else:
            print("There are no items in your bag")
        player1.print()
    else:
        print("Enter a valid action.")
    if  activeRoom.enemies:
        for enemy in activeRoom.enemies:
            player1.takeDamage(enemy.dealDamage(),enemy.getName())
    
    for i in range(20):
        print("+", end=" ", flush=True)
        time.sleep(0.1)
    print("")