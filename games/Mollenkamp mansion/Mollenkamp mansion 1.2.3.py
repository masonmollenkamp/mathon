import sys
import random
import os
import time
os.system('cls')
help = "List of commands:\n1.inspect or examine, type one and then the item name\n2.interact or use, type one and then the item name\n3.unlock or open, type one and then the room name\n4.goto or move type on and then the room\n5. attack ot hit type one and the item name\n you can also use exec to run python commands to mess with the game, don't have too much fun though"
print(help)

commandList = [] #list of commands
invatory = [""]
currentRoom = "redroom"
gameIteration = 1
Quit = False
computerDone = False
Bannana = True

rooms = {"Testroom" :
         {
           "Locked"  :
            "unlocked", 
            "Bed" :
              ["it's a bed", {
                  "sleep " : "Sleeping...", "jhgdfsjf " : "hjrfgrjdfghrj f"}],
            "phone" :
              ["its a phone", {
                  "unlock" : "print('this concludes the test')\nprint('everything is awsome')"},
                   10,
                    {8 : "tiny crack", 7 : "pretty big crack", 6 : "crack across the screen", 5 : "multiple scrtches and one huge crack", 4 : "2 Huge Cracks", 3 : "Display broken", 2 : "Screen detached", 1 : "bits and pieces"}]
            },
         "redroom" :
         {
             "Locked" : "unlocked",
             "SSD" :
             ["it's a table", {"unscrew" : """rooms[\"redroom\"].update({\"Badge\" : [\"it can go into one of the slots in the jacket.\", {\"Put pin in holes\" : \"\"\"if computerDone == 1 && input(\\\"which hole\\\") == 4:
	print(\\\"The right latch on the white door is open\\\")
	badge = True\"\"\"}]})"""}],
             "computer" :
             ["it's a computer", {"login" : "print(\"The computer seems to be locked and it gives you a password hint: The fourth hole\")\ncomputerDone = 1"}, 0, {1 : "A note falls out of the computer, it reads 'hello i see you have smashed the only way to get out of here oh well"}]},
         "jacket" :
             ["it's a jacket", {"" : "print(\"\")"}, 0, {1 : "You hit the jacket, nothing happened, What did you expect"}]}, 
"blueroom" :
     
         {
             "Locked" : "unlocked",
             "Saw" : ["it's just a saw", {"litraly nothing" : "print(\"seriosly\")"}, 2, {1 : "the saw won't snap"}],
             "computer" : ["no logo", {"use another item" : """if (input(\"What item\") == \"saw\"):
    Bannana = True
    os.system('echo Welcome to BannanaOS, Type help or a command')
    print(\"You use the saw to cut a bannana silhouette out of the side of the computer so you can put the bannana inside. when you put the bannana in the light on the front of the computer ligths up and the left latch of the white door is open.\")
else: 
    print(\"Nothing Happens\")""", "play on computer" : "print(\"You get on the computer. A file called Mollenkamp mansion opens up, then you relize that the computer is your computer and an error message occurs on your computer. Hmm, you'll need a new app to open this error link... Aha! it means that the programers made a mistake!\")\nfor i in range(5):\n  os.system(\'start \\\"Mollenkamp mansion.py\\\"\\\necho Error: Virus detected.\')"},
             0, {1 : "its a computer do you think your going to smash it with your bare hand?"}],
             "bananas" : ["there are three of them", {"eat" : "print(\"Attack the bannanas to eat them.\")"}, 2, {1 : "There are 2 of them"}]}
    }


def doGameItaration():
    global gameIteration

    commandList = [] #reset list of commands

    
    #for every room get every items every command and make a list like this [[play games, phone], [login, computer]]
    for room in rooms: 
        for item in rooms[room]:
            for command in rooms[room][item][1]:
                commandList.append([command, item])
    
    #prints all items in all rooms
    for room in rooms:
        print(room + "contains:")
        #See 'Why list is slow.mp4'
        for item in rooms[room]:
            if item != "Locked":
                print(item) 
        print()
    if gameIteration == 1:
        print("Player wakes up in their normal room, but it feels wobbly. They go and open their door and see a sign in a white room ‘Pick a door red or blue, there is a white door in front of them, to the left there is a red and a blue door.")
    elif gameIteration == 2:
        print("The room seems to be themed around bannana(C) the computer company")
        if computerDone == True  &  Bannana == "*":
            gameIteration == 4
            doGameItaration

def Examine(item):
    global currentRoom
    global commandList

    #the list of commands
    examineItem = []

    for Command in commandList: # commandList is a var of all commands
        if Command[1] == item: #The [1] gets the item this command can be used on
            examineItem += Command[0]

    print(rooms[currentRoom][item][0]) #prints a discription of the item
    print("You can:")

    #converts list into string
    y = ""
    for i in range(len(examineItem)):

        y += examineItem[i] 
    print(y)

    print("With this item.")

def moveRoom(x):        
    global currentRoom
    global rooms
    global gameIteration

    #helps find what error happened
    Error = []

    for room in rooms:
        if x == room:
            if rooms[x]["Locked"] == "unlocked":
                currentRoom = x
                print(x)
                if x == "blueroom":
                    gameIteration = 2 #Game iteration text changes to bluerooms
                elif x == "redroom":
                    gameIteration = 3 #or redrooms
            else:
                Error.append("*")
        else:
            Error.append("")
    if Error == ["*"]:
        print("Locked") 
    print("You are now in {}".format(currentRoom))
    #dont print the value locked only print the items
    for item in rooms[currentRoom]:
        if {"Locked" : "unlocked"} != item:
            print(item)

def unlock(room):
    global invatory
    global rooms
    #look throught every item in invotory
    for item in invatory:
        # the first word is the room you want to unlock it unlockes
        if item.split(" ")[0] == room:
            rooms[room]["Locked"] = "unlocked"
            print("unlocked")
        else:
            print("no key")

def interact(item, command):
    try:
        #try to execute the value (a python command) of the item in your room
        exec(rooms
            [currentRoom]
            [item][1]
            [command])
    except Exception as e:
        #if this appears you did not enter a correct item or command
        print("Error, that is not an item or that is not a command {}".format(e))

def attack(item, type):
    #for items in your room
    for forLoopItem in rooms[currentRoom]:
        #if you are attacking that item
        if item == forLoopItem:
            #if you use specail you get a rand dammage, but if not then you get 5, or if  your dammage is greater than the health of the enemy than it sets it to 1
            if type == True:
                Dammage = random.randint(2,8)
                if Dammage < rooms[currentRoom][item][2]:
                    rooms[currentRoom][item][2] = rooms[currentRoom][item][2] - Dammage
                    rooms[currentRoom][item][0] = rooms[currentRoom][item][3][rooms[currentRoom][item][2]]
                else:
                    rooms[currentRoom][item][2] = 1
                    rooms[currentRoom][item][0] = rooms[currentRoom][item][3][rooms[currentRoom][item][2]]
            else:
                if 5 < rooms[currentRoom][item][2]:
                    rooms[currentRoom][item][2] = rooms[currentRoom][item][2] - 5
                    rooms[currentRoom][item][0] = rooms[currentRoom][item][3][rooms[currentRoom][item][2]]
                else:
                    rooms[currentRoom][item][2] = 1
                    rooms[currentRoom][item][0] = rooms[currentRoom][item][3][rooms[currentRoom][item][2]]
    return rooms[currentRoom][item][0]


#system to save
try:
    gameIteration = eval(input("Put in a password or just press enter."))
except SyntaxError:
    gameIteration = 1

if gameIteration == "":
    gameIteration == 1

while Quit != True:
    #gives time for people to read, clears the screen, does GameItration and gets an input fo the command
    time.sleep(5)
    os.system("cls")
    doGameItaration()
    Command = ""
    Command = input()

    #Try to exexecute a known command otherwise print an error
    try:
        if Command.split(" ")[0] == "inspect" or Command.split(" ")[0] == "examine":
            Examine(Command.split(" ")[1])
        elif Command.split(" ")[0] == "interact" or Command.split(" ")[0] == "use":
            x = ""
            for item in Command.split(" ")[2:]:
                if len(Command.split(" ")[2:]) != (Command.split(" ")[2:].index(item) + 1):
                    x += item + " "  
                else:
                    x = x + item
            interact(Command.split(" ")[1], x)
        elif Command.split(" ")[0] == "unlock" or Command.split(" ")[0] == "open":
            unlock(Command.split(" ")[1])
        elif Command.split(" ")[0] == "goto" or Command.split(" ")[0] == "move":
            moveRoom(Command.split(" ")[1])
        elif Command.split(" ")[0] == "hit" or Command.split(" ")[0] == "attack":
            attack(Command.split(" ")[1], True) if Command.split(" ")[2] == True else attack(Command.split(" ")[1], False)
        else:
            print(help)
    except Exception as e:
        print("An error has occured. {}".format(e))