#!/usr/bin/python3

# Eingabe
eingabe_str = input("Bitte geben Sie eine Zahl ein: ")

# Verarbeitung
# Funktionen:

# isNumber() ist eine Funktion und nimmt einen Text entgegen und es wird versucht ein float-Cast durchzufuehren
# Sollte kein ValueError auftreten ist es umwandelbar in ein float und somit eine Zahl
# Der Rueckgabewert ist True wenn es eine Zahl ist und False wenn es keine Zahl ist
def isNumber(text):
    try:
        float(text)
        return True
    except ValueError: #Bonus: Hier wird explizit der Fehler ValueError abgefangen
        print("Es ist keine Zahl eingegeben worden")
        return False
    except:
        print("Es ist ein genereller Fehler aufgetreten")
        return False


# Ausgabe
# Hier muss die funktion isNumber() noch aufgerufen werden, da es einen Rueckgabewert von True oder False hat,
# duerfen Sie die Funktion als Bedingung einbauen
if isNumber(eingabe_str):
    print("Es wurde eine korrekte Zahl eingegeben: " + eingabe_str)
else:
    print("Es wurde folgender Text eingegeben: " + eingabe_str)