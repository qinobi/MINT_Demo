#!/usr/bin/python3

# Imports
import random

#Initialisierung globaler Variablen:

gameState = True
winState = False
hiddenCode = ""
guessCounter = 0
numberCount = []

#Funktionen
# Mit dieser Funktion können Sie den Code manuell Setzen
def initializeGame(code):
    #mit dem Keyword global bereiten wir vor, dass wir die Variablen ausserhalb der Funktion verändern möchten
    global hiddenCode 
    global winState
    global guessCounter
    winState = False
    guessCounter = 0
    hiddenCode = code
    setNumberCount(code)

# Mit dieser Funktion wird eine Zufallscode generiert
def initializeRandomGame():
    # Hier wäre ein Beispiel für einen Zufallsgenerator:
    # aus dem paket random wird die randint() Funktion aufgerufen
    # als Parameter können start und ende einer Range angegeben werden, die endzahl ist inklusive
    # Zufallszahl zwischen 0 und 9999(inkl) erstellen 
    zufallsZahl = random.randint(0, 9999)
    # Zufallszahl als Text abspeichern
    generatedCode = str(zufallsZahl)
    # Solange der Code kleiner ist als ein vierstelliger Code solange ergaenzt bis er vierstellig ist.
    while (len(generatedCode) < 4):
        generatedCode = "0" + generatedCode

    initializeGame(generatedCode)
    
def inputOK(text):
    return len(text) == 4 and text.isdigit()
    
def inputLoop():
    global guessCounter
    eingabe = ""
    while(not inputOK(eingabe)):
        eingabe = input("Bitte geben Sie einen gueltigen Code ein: ")
    guessCounter += 1
    return eingabe

def restartGameLoop():
    eingabe = ""
    while(not (eingabe == "y" or eingabe == "n")):
        eingabe = input("Nochmals spielen? (y/n): ")
    return eingabe

def checkCode(code):
    global winState
    if hiddenCode == code:
        winState = True
        print("Gratuliere, Sie haben gewonnen der Code war ", hiddenCode)
        print("Sie haben", guessCounter, "Versuch(e) gebraucht.")

def feedback(code):
    tempNumberCount = numberCount
    feedback = ""
    for i in range(4):
        if code[i] == hiddenCode[i]:
            feedback += "@"
        elif hiddenCode.find(code[i]) == -1:
            feedback += "X"
        else:
            if tempNumberCount[int(code[i])] > 0:
                tempNumberCount[int(code[i])] -= 1
                feedback += "O"
            else:
                feedback += "X"  
    print(feedback)

def setNumberCount(code):
    global numberCount
    numberCount = [0,0,0,0,0,0,0,0,0,0]
    for i in range(len(code)):
        numberCount[int(code[i])] += 1
       


#Spiel Initialisierung
initializeRandomGame()

#Game Schleife
while(gameState):
    while(not winState):
        eingabe = inputLoop()
        feedback(eingabe)
        checkCode(eingabe)
    restart = restartGameLoop()
    if  restart == "n":
        gameState = False   
    else:
        initializeRandomGame()


