import time


def mainMenu():
  while True:
    print("----------------")
    print("Options:")
    print("1. Console RPG")
    print("2. Info")
    print("3. Update Log")
    print("4. Bug Fixes")
    mainMenuInput = input("Enter a number from the showen list above.   >>")
    if mainMenuInput == "1":
      print("Console RPG will now load!")
      break
    elif mainMenuInput == "2":
      print("This RPG is text-based. You'll need a bit of imagenation to make up for it.")
      time.sleep(5)
    elif mainMenuInput == "3":
      __file__ = open("updateLog.txt", "r")
      print("---Update Log---")
      print(__file__.read())
      __file__.close()
      print("---End of Log---")
    elif mainMenuInput == "4":
      __file__ = open("bugFixes.txt", "r")
      print("---Bug Fixes---")
      print(__file__.read())
      __file__.close()
      print("End of log")
    else:
      print("Not valid input, try again! Your input should look like '3' or '2'")
  print("------BEGINNING GAME------")
