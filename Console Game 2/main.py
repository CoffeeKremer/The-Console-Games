import time
import random

from BootScreen import mainMenu

print("Hello, User.")
mainMenu()

Regionx = 0
Regiony = 0

strength = 1
health = 20
defence = 0
maxHP = 20
level = 0

BossDefeated = False
BossDefeatPlayer = False

xp = 0
heals = 0


def region(x,y):
    global heals
    global xp
    hasFought = False
    hasLooted = False
    luck = random.randint(1,10)
    
    if x == 0 and y == 0:
        while True:
            print("Options for this region:")
            print("1. Fight")
            print("2. Scavange")
            print("3. Exit region")
            choice = input(">>")
        
            if choice == "1":
                if hasFought == False:
                    battle(20, 0, 1, 1, False)
                    hasFought = True 
                else:
                    print("You already tried to fight.")
            elif choice == "2":
                if hasLooted == False:
                    if luck >= 4:
                        heals += 1
                        print("You found a healing item.")
                        hasLooted = True
                    else:
                        print("You got nothing.")
                        hasLooted = True
                else:
                    print("You have already looted this region!")
            elif choice == "3":
                break
            else:
                print("Invalid choice!")
                
    elif x == 0 and y == -1:
        while True:
            print("Options for this region:")
            print("1. Fight")
            print("2. Scavange")
            print("3. Exit region")
            choice = input(">>")
        
            if choice == "1":
                if hasFought == False:
                    battle(30, 2, 1, 3, False)
                    hasFought = True 
                else:
                    print("You already tried to fight.")
            elif choice == "2":
                if hasLooted == False:
                    if luck >= 8:
                        xp += 40
                        print("You found a flask of liquid experience.")
                        hasLooted = True
                    else:
                        print("You got nothing.")
                        hasLooted = True
                else:
                    print("You already looted this area")
            elif choice == "3":
                break
            else:
                print("Invalid choice!")
                
    elif x == 0 and y == 1:
        while True:
            print("Options for this region:")
            print("1. Fight")
            print("2. Scavange")
            print("3. Exit region")
            choice = input(">>")
        
            if choice == "1":
                if hasFought == False:
                    battle(20, 5, 2, 6, False)
                    hasFought = True 
                else:
                    print("You already tried to fight.")
            elif choice == "2":
                print("The land is barren, there is nothing here.")
            elif choice == "3":
                break
            else:
                print("Invalid choice!")
    
    elif x == -1 and y == 0:
        while True:
            print("Options for this region:")
            print("1. Fight")
            print("2. Scavange")
            print("3. Exit region")
            choice = input(">>")
        
            if choice == "1":
                if hasFought == False:
                    batttle(30, 5, 1, 6, False)
                    hasFought = True 
                else:
                    print("You already tried to fight.")
            elif choice == "2":
                if hasLooted == False:
                    if luck >= 8:
                        heals += 2
                        print("You found a healing item.")
                    elif luck <= 3:
                        xp += 20
                        print("You found a small bottle of liquid experience!")
                    else:
                        print("You got nothing.")
                else:
                    print("You have already looted this region.")
            elif choice == "3":
                break
            else:
                print("Invalid choice!")
    
    elif x == -1 and y == -1:
        while True:
            print("Options for this region:")
            print("1. Fight")
            print("2. Scavange")
            print("3. Exit region")
            choice = input(">>")
        
            if choice == "1":
                if hasFought == False:
                    battle(40, 5, 3, 10, False)
                    hasFought = True 
                else:
                    print("You already tried to fight.")
            elif choice == "2":
                if hasLooted == False:
                    if luck == 5:
                        heals += 3
                        print("You found a healing item.")
                    else:
                        print("You got nothing.")
                else:
                    print("You already looted this region")
            elif choice == "3":
                break
            else:
                print("Invalid choice!")
    elif x == -1 and y == 1:
        while True:
            print("Options for this region:")
            print("1. Fight")
            print("2. Scavange")
            print("3. Exit region")
            choice = input(">>")
        
            if choice == "1":
                print("It seems to be peaceful here.")
            elif choice == "2":
                print("There doesn't appear to be anything here.")
            elif choice == "3":
                break
            else:
                print("Invalid choice!")
    
    elif x == 1 and y == -1:
        while True:
            print("Options for this region:")
            print("1. Fight")
            print("2. Scavange")
            print("3. Exit region")
            choice = input(">>")
        
            if choice == "1":
                if hasFought == False:
                    battle(50, 5, 3, 11, False)
                    hasFought = True 
                else:
                    print("You already tried to fight.")
            elif choice == "2":
                if hasLooted == False:
                    if luck >= 7:
                        heals += 1
                        print("You found a healing item.")
                    elif luck < 5:
                        xp += 20
                        print("You found a small bottle of xp.")
                    else:
                        print("You got nothing.")
                else:
                    print("You have already looted this region.")
            elif choice == "3":
                break
            else:
                print("Invalid choice!")

    elif x == 1 and y == 0:
        while True:
            print("Options for this region:")
            print("1. Fight")
            print("2. Scavange")
            print("3. Exit region")
            choice = input(">>")
        
            if choice == "1":
                print("There are no enemies in this area.")
            elif choice == "2":
                if hasLooted == False:
                    if luck >= 9:
                        xp += 80
                        print("You found a large bottle of liquid xp.")
                    elif luck == 5:
                        heals += 1
                        print("You found a healing item.")
                    elif luck > 5:
                        xp += 20
                        print("You found a small bottle of xp.")
                    else:
                        print("You got nothing.")
                else:
                    print("You already looted this region.")
            elif choice == "3":
                break
            else:
                print("Invalid choice!")
                
    elif x == 1 and y == 1:
        while True:
            print("Options for this region:")
            print("1. Fight")
            print("2. Scavange")
            print("3. Exit region")
            choice = input(">>")
        
            if choice == "1":
                if hasFought == False:
                    battle(30, 10, 1, 11, False)
                    hasFought = True 
                else:
                    print("You already tried to fight.")
            elif choice == "2":
                print("There is nothing scavenge-able")
            elif choice == "3":
                break
            else:
                print("Invalid choice!")
    
    elif x == -2 and y == 0:
        print("This is the boss")
        battle(500, 10, 1, 100, True)


def battle(EnHP, EnDef, EnStr, EnLVL, Boss):
    global xp
    global heals
    global health
    global BossDefeated
    global BossDefeatPlayer
    monesterAlive = True
    playerAlive = True
    PlayerDodgeNextAttack = False 
    
    EnemyHealth = EnHP
    EnemyDefence = EnDef
    EnemyStrength = EnStr
    EnemyLevel = EnLVL
    
    InBattle = True
    
    while True:
        if playerAlive == False:
            if BossDefeatPlayer == False
                print("You have fallen unconscious, you'll wake up later...")
                break
            else:
                print("Game over.")
        else:
            while True:
                print("----Battle Options----")
                print("1. Attack")
                print("2. Dodge")
                print("3. Query Enemy Stats")
                print("4. Your Stats")
                print("5. Heal")
                print("6. Exit")
                choice = input(">>")
                
                if choice == "1":
                    attMult = random.randint(1,3)
                    YourDMG = strength * attMult
                    actDMG = YourDMG - EnemyDefence
                    if actDMG < 0:
                        actDMG = 0
                    EnemyHealth -= actDMG
                    print("You swing your sword with", str(YourDMG), "but only deal", str(actDMG), "to the enemy.")
                    time.sleep(1)
                    break
                elif choice == "2":
                    DodgeChance = random.randint(1,10)
                    if DodgeChance < 4:
                        print("Your legs don't seem ready to dodge.")
                        time.sleep(1)
                        break
                    else:
                        print("You are ready to dodge.")
                        PlayerDodgeNextAttack = True
                        time.sleep(1)
                        break
                elif choice == "3":
                    print("Enemy Health:", str(EnemyHealth))
                    print("Enemy Defence:", str(EnemyDefence))
                    print("Enemy Strength:", str(EnemyStrength))
                    time.sleep(2)
                    continue
                elif choice == "4":
                    print("HP:", str(health))
                    print("Defence:", str(defence))
                    print("Strength:", str(strength))
                    print("You have", str(heals), "heals.")
                    time.sleep(2)
                    continue
                elif choice == "5":
                    if heals > 0:
                        heals -= 1
                        health += 20
                        if health > maxHP:
                            health = maxHP
                        print("You heal for 20 HP")
                        continue
                    else:
                        print("You don't have any heals!")
                elif choice == "6":
                    if Boss == False:
                        InBattle = False
                    else:
                        print("You can't leave!")
                else:
                    print("Invalid/unreconized input.")
        if InBattle == False:
            break

        if EnemyHealth <= 0:
            monesterAlive = False
        
        if monesterAlive == False:
            ("You have beaten the monester!")
            xpGained = EnemyLevel * 10 + EnemyStrength
            xp += xpGained
            print("You gained", str(xp), "xp.")
            time.sleep(2)
            if Boss == True:
                BossDefeated = True
            break
        else:
            if PlayerDodgeNextAttack == False:
                attMult = random.randint(1,2)
                YourDMG = EnemyStrength * attMult
                actDMG = YourDMG - defence
                if actDMG < 0:
                    actDMG = 0
                health -= actDMG
                print("The enemy swings its sword with", str(YourDMG), "damage but it only deals", str(actDMG), "to you.")
                time.sleep(2)
            else:
                print("You dodged the enemy's attack.")
                PlayerDodgeNextAttack = False
                time.sleep(1)
                
        if health <= 0:
            if Boss == False:
                playerAlive = False
                health = 1
            else:
                BossDefeatPlayer = True
    

def regionSwitch(x,y):
    global Regionx
    global Regiony
    if x == 0 and y == 0:
        print("Which direction would you like to go?")
        print("1. North")
        print("2. East")
        print("3. South")
        print("4. West")
        choice = input(">>")
        
        if choice == "1":
            Regiony += 1
        elif choice == "2":
            Regionx += 1
        elif choice == "3":
            Regiony -= 1
        elif choice == "4":
            Regionx -= 1
        else:
            print("Invalid Input")

    elif x == 0 and y == 1:
        print("Which direction would you like to go?")
        print("1. East")
        print("2. South")
        print("3. West")
        choice = input(">>")
        
        if choice == "1":
            Regionx += 1
        elif choice == "2":
            Regiony -= 1
        elif choice == "3":
            Regionx -= 1
        else:
            print("Invalid Input")
    
    elif x == 0 and y == -1:
        print("Which direction would you like to go?")
        print("1. North")
        print("2. East")
        print("3. West")
        choice = input(">>")
        
        if choice == "1":
            Regiony += 1
        elif choice == "2":
            Regionx += 1
        elif choice == "3":
            Regionx -= 1
        else:
            print("Invalid Input")
    
    elif x == -1 and y == 0:
        print("Which direction would you like to go?")
        print("1. North")
        print("2. East")
        print("3. South")
        print("4. West (BOSS! Note: When you start the boss, you can't leave! Boss Stats: 500 Hp, 10 Def, 1 Str)")
        choice = input(">>")
        
        if choice == "1":
            Regiony += 1
        elif choice == "2":
            Regionx += 1
        elif choice == "3":
            Regiony -= 1
        elif choice == "4":
            Regionx -= 1
        else:
            print("Invalid Input")

    elif x == -1 and y == -1:
        print("Which direction would you like to go?")
        print("1. North")
        print("2. East")
        choice = input(">>")
        
        if choice == "1":
            Regiony += 1
        elif choice == "2":
            Regionx += 1
        else:
            print("Invalid Input")
    
    elif x == -1 and y == 1:
        print("Which direction would you like to go?")
        print("2. East")
        print("3. South")
        choice = input(">>")
        
        if choice == "1":
            Regionx += 1
        elif choice == "2":
            RegionY -= 1
        else:
            print("Invalid Input")
    
    elif x == 1 and y == 0:
        print("Which direction would you like to go?")
        print("1. North")
        print("2. South")
        print("3. West")
        choice = input(">>")
        
        if choice == "1":
            Regiony += 1
        elif choice == "2":
            Regiony -= 1
        elif choice == "3":
            Regionx -= 1
        else:
            print("Invalid Input")
            
    elif x == 1 and y == -1:
        print("Which direction would you like to go?")
        print("1. North")
        print("2. West")
        choice = input(">>")
        
        if choice == "1":
            Regiony += 1
        elif choice == "2":
            Regionx -= 1
        else:
            print("Invalid Input")
    
    elif x == 1 and y == 1:
        print("Which direction would you like to go?")
        print("1. South")
        print("2. West")
        choice = input(">>")
        
        if choice == "1":
            Regiony -= 1
        elif choice == "2":
            Regionx -= 1
        else:
            print("Invalid Input")


def levelUp():
    global strength
    global maxHP
    global defence
    global level
    global xp
    global health
    
    while True:
        print("--------------------")
        print("You have enough xp for a level up!")
        print("---Select Upgrade---")
        print("1. Strength Upgrade (+1 Strength)")
        print("2. Defence Upgrade (+1 Defence)")
        print("3. Health Upgrade (+10 Health")
        choice = input(">>")
        
        if choice == "1":
            strength += 1
            xp -= 50
            level += 1
            print("You feel stronger")
            time.sleep(2)
            break
        elif choice == "2":
            defence += 1
            xp -= 50
            level += 1
            print("You feel tankier")
            time.sleep(2)
            break
        elif choice == "3":
            maxHP += 10
            xp -= 50
            level += 1
            health = maxHP
            print("Your health will last you longer, and you have been healed!")
            time.sleep(2)
            break
        else:
            print("Invalid Input!")
        

def ending():
    print("----Stats----")
    time.sleep(1)
    print("You got to level", str(level), "!")
    time.sleep(2)
    print("Your max HP was at:", str(maxHP), "!")
    time.sleep(2)
    print("You had", str(strength), "points in strength.")
    time.sleep(2)
    print("You had", str(defence), "points in defence.")
    time.sleep(2)
    print("You had", str(heals), "heals left over.")
    time.sleep(2)
    print("-------------")
    
while True:
    region(Regionx, Regiony)
    if BossDefeated == False or BossDefeatPlayer == False:
        while xp >= 50:
            levelUp()
            
        regionSwitch(Regionx, Regiony)
    else:
        print("Thanks for playing!")
        ending()
        break