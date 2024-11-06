def mainMenu():
    while True:
        print("----------")
        print("Pick an option:")
        print("1. Begin")
        print("2. Update Log")
        print("3. Bug Fixes.")
        mainMenuInput = input("Option: ")
        if mainMenuInput == "1":
            print("The game will now load...")
            break
        elif mainMenuInput == "2":
            __file__ = open("updateLog.txt", "r")
            print("---Update Log---")
            print(__file__.read())
            __file__.close()
            print("---End of Log---")
        elif mainMenuInput == "3":
            __file__ = open("bugFixes.txt", "r")
            print("---Fix Log---")
            print(__file__.read())
            __file__.close()
            print("---End of Log---")
        else:
            print("Not a vaild input.")
            continue