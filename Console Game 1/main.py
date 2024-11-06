import random
import time

from startUp import mainMenu

gold = 0
lanternFuel = 2.5
FUELCONSUMPTIONBASERATE = 0.5
lanternFuelMax = 10
RoomSearched = False
searchedRooms = 0
score = 0
TimesTrolled = 0
exchanged = False
timesExchanged = 0

print("Booting up...")
time.sleep(1)
mainMenu()

file = open("BeginningStory.txt", "r")
print(file.read())
file.close()
time.sleep(3)


def room1():
  global lanternFuel
  global gold
  global RoomSearched
  global searchedRooms
  global score
  FuelCheck = lanternFuel - (FUELCONSUMPTIONBASERATE * darkness)
  
  if darkness <= 2:
    print("This room isn't very dark.")
  elif 3 >= darkness == 4:
    print("This room is kinda dark. I'll have to use more fuel!")
  elif darkness == 5:
    print("This room has no light! I'll have to set my lantern to max!")
  
  while True:
    print("---Actions---")
    print("1. Search the room. (Requires lantern fuel!)")
    print("2. Continue up the stairs.")
    print("3. Check lantern fuel.")
    action = input("Number Choice: ")
  
    if action == "1":
      if not RoomSearched:
        if FuelCheck > 0:
          luck = random.randint(1, 20)
          lanternFuel = lanternFuel - (FUELCONSUMPTIONBASERATE * darkness)
          if luck <= 7:
            print("You found nothing.")
            RoomSearched = True
            searchedRooms += 1
          elif 7 < luck <= 15:
            print("You found some gold coins, 15 to be exact.")
            gold += 15
            RoomSearched = True
            searchedRooms += 1
            score += 15
          elif  15 < luck <= 18:
            print("You found a tank of lantern fuel, it's about 30% full.")
            lanternFuel += 3
            RoomSearched = True
            searchedRooms += 1
            score += 15
          else:
            print("You found a lantern fuel tank, it's about 50% full.")
            lanternFuel += 5
            RoomSearched = True
            searchedRooms += 1
            score += 30
        else:
          print("You don't have enough lantern fuel to search this room.")
      else:
        print("You've already searched this room.")
    elif action == "2":
      print("You continue to the next room.")
      for _i in range(5):
        print("")
      break
    elif action == "3":
      print("You have", str(lanternFuel * 10), "% lantern fuel left.")
    else:
      print(action, "is not a valid choice.")
      continue

def room2():
  global lanternFuel
  global gold
  global RoomSearched
  global searchedRooms
  global score
  
  print("There is light in this room!")
  while True:
    print("---Actions---")
    print("1. Search the room.")
    print("2. Continue up the stairs.")
    print("3. Check lantern fuel.")
    action = input("Number Choice: ")

    if action == "1":
      if not RoomSearched:
        luck = random.randint(1, 2)
        if luck == 1:
          print("You found a lantern fuel tank, it's about 20% full.")
          lanternFuel += 2
          RoomSearched = True
          searchedRooms += 1
          score += 30
        else:
          print("You found 5 gold coins.")
          gold += 5
          RoomSearched = True
          searchedRooms += 1
          score += 5
      else:
        print("You've already searched this room.")
    elif action == "2":
      print("You continue to the next room.")
      for _i in range(5):
        print("")
      break
    elif action == "3":
      print("You have", str(lanternFuel * 10), "% lantern fuel left.")
    else:
      print(action, "is not a valid choice.")
      continue

def room3():
  global lanternFuel
  global gold
  global RoomSearched
  global searchedRooms
  global score
  FuelCheck = lanternFuel - (FUELCONSUMPTIONBASERATE * 6)

  print("This room is impossiably dark! I can't see without my lantern!")
  while True:
    print("---Actions---")
    print("1. Search the room. (Requires lantern fuel!)")
    print("2. Continue up the stairs.")
    print("3. Check lantern fuel.")
    action = input("Number Choice: ")

    if action == "1":
      if not RoomSearched:
        if FuelCheck > 0:
          luck = random.randint(1, 20)
          lanternFuel = lanternFuel - (FUELCONSUMPTIONBASERATE * darkness)
          if luck <= 7:
            print("You found 30 gold coins.")
            RoomSearched = True
            searchedRooms += 1
            gold += 30
            score += 30
          elif 7 < luck <= 15:
            print("You found many gold coins, 45 to be exact.")
            gold += 45
            RoomSearched = True
            searchedRooms += 1
            score += 45
          elif  15 < luck <= 18:
            print("You found a tank of lantern fuel, it's about 30% full.")
            lanternFuel += 3
            RoomSearched = True
            searchedRooms += 1
            score += 15
          else:
            print("You found a lantern fuel tank, it's about 50% full.")
            lanternFuel += 5
            RoomSearched = True
            searchedRooms += 1
            score += 30
        else:
          print("You don't have enough lantern fuel to search this room.")
      else:
        print("You've already searched this room.")
    elif action == "2":
      print("You continue to the next room.")
      for _i in range(5):
        print("")
      break
    elif action == "3":
      print("You have", str(lanternFuel * 10), "% lantern fuel left.")
    else:
      print(action, "is not a valid choice.")
      continue

def room4():
  global lanternFuel
  global gold
  global RoomSearched
  global searchedRooms
  global score
  global TimesTrolled
  FuelCheck = lanternFuel - (FUELCONSUMPTIONBASERATE * darkness)

  if darkness <= 2:
    print("This room isn't very dark.")
  elif 3 >= darkness >= 4:
    print("This room is kinda dark. I'll have to use more fuel!")
  elif darkness == 5:
    print("This room has no light! I'll have to set my lantern to max!")

  while True:
    print("---Actions---")
    print("1. Search the room. (Requires lantern fuel!)")
    print("2. Continue up the stairs.")
    print("3. Check lantern fuel.")
    action = input("Number Choice: ")

    if action == "1":
      if not RoomSearched:
        if FuelCheck > 0:
          luck = random.randint(1, 20)
          lanternFuel = lanternFuel - (FUELCONSUMPTIONBASERATE * darkness)
          if luck <= 3:
            print("You find a piece of paper. The image on it looks odd. ")
            time.sleep(2)
            print("It jumps at you with a 'trolololololol' sound.'")
            time.sleep(2)
            print("You lose 30 gold coins.")
            RoomSearched = True
            searchedRooms += 1
            gold -= 30
            score -= 30
            TimesTrolled += 1
          elif 3 < luck <= 10:
            print("You found some gold coins, 5 to be exact.")
            gold += 5
            RoomSearched = True
            searchedRooms += 1
            score += 5
          elif  10 < luck <= 15:
            print("You found a tank of lantern fuel, it's about 10% full.")
            lanternFuel += 1
            RoomSearched = True
            searchedRooms += 1
            score += 5
          else:
            print("You found a lantern fuel tank, it's about 20% full.")
            lanternFuel += 2
            RoomSearched = True
            searchedRooms += 1
            score += 10
        else:
          print("You don't have enough lantern fuel to search this room.")
      else:
        print("You've already searched this room.")
    elif action == "2":
      print("You continue to the next room.")
      for _i in range(5):
        print("")
      break
    elif action == "3":
      print("You have", str(lanternFuel * 10), "% lantern fuel left.")
    else:
      print(action, "is not a valid choice.")
      continue

def room5():
  global lanternFuel
  global gold
  global RoomSearched
  global searchedRooms
  global score
  global exchanged
  global timesExchanged
  print("This room has a fuel exchange.")

  while True:
    print("---Actions---")
    print("1. Exchange")
    print("2. Continue up the stairs.")
    print("3. Check lantern fuel.")
    print("4. Check gold.")
    action = input("Number Choice: ")

    if action == "1":
      if not exchanged:
        print("-! YOU CAN ONLY EXCHANGE ONCE !-")
        print("---Exchange---")
        print("1. Buy 30 gold for 25% lantern fuel? ")
        print("2. Buy 25% lantern fuel for 30 gold?")
        print("3. Return")
        exchangeType = input("What would you like to exchange? >>")
        if exchangeType == "1":
          if lanternFuel >= 2.5:
            gold += 30
            lanternFuel -= 2.5
            exchanged = True
            timesExchanged += 1
            print("You exchanged 25% lantern fuel for 30 gold.")
          else:
            print("You don't have enough gold for the exchange.")
        elif exchangeType == "2":
          if gold >= 30:
            lanternFuel += 2.5
            gold -= 30
            exchanged = True
            timesExchanged += 1
            print("You exchanged 30 gold for 25% lantern fuel.")
          else:
            print("You don't have enough lantern fuel to exchange.")
        elif exchangeType == "3":
          continue
        else:
          print("Not a valid input.")
      else:
        print("You've already exchanged in this room!")
    elif action == "2":
      print("You continue to the next room.")
      for _i in range(5):
        print("")
      break
    elif action == "3":
      print("You have", str(lanternFuel * 10), "% lantern fuel left.")
    elif action == "4":
      print("You have", str(gold), "gold.")
    else:
      print(action, "is not a valid choice.")
      continue

# Main Game loop begins below.
for _i in range(20):
    darkness = random.randint(1, 5)
    RoomSearched = False
    exchanged = False
    time.sleep(2)
    roomPicker = random.randint(1, 5)
    if roomPicker == 1:
      room1()
    elif roomPicker == 2:
      room2()
    elif roomPicker == 3:
      room3()
    elif roomPicker == 4:
      room4()
    else:
      room5()

print("You reached to top of the tower! You plant your flag on pole.")
time.sleep(3)
print("----Post Game Stats----")
time.sleep(1)
if TimesTrolled > 0:
  print("You've been trolled,", str(TimesTrolled),"times.")
  time.sleep(1)
  print("www.youtube.com/watch?v=PXqcHi2fkXI")
print("You exchaned items", str(timesExchanged), "times.")
time.sleep(1)
print("You've collected", str(gold), "gold coins.")
time.sleep(1)
print("You've searched", str(searchedRooms), "rooms.")
time.sleep(1)
print("You got a score of:", str(score), "points.")
time.sleep(2)
print("Thanks for playing my short game.")
print("This window will automatically close in 60 seconds!")
time.sleep(60)
