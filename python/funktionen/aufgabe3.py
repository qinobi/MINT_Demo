#!/usr/bin/python3


# Funktionen koennen Sie auch vor der Eingabe definieren:

# isNumber() ist eine Funktion und nimmt einen Text entgegen und es wird versucht ein float-Cast durchzufuehren
# Sollte kein ValueError auftreten ist es umwandelbar in ein float und somit eine Zahl
# Der Rueckgabewert ist True wenn es eine Zahl ist und False wenn es keine Zahl ist
def isNumber(text):
    try:
        float(text)
        return True
    except ValueError: #Bonus: Hier wird explizit der Fehler ValueError abgefangen
        print(text, "ist keine Zahl.")
        return False
    except:
        print("Es ist ein genereller Fehler aufgetreten")
        return False


# Programm Initialisierung:
print("Dieses Programm ermittelt welche von zwei Zahlen die groessere ist.")

# Eingabe
eingabe1 = input("Geben Sie die Erste Zahl ein: ")
eingabe2 = input("Geben Sie die Zweite Zahl ein: ")

# Verarbeitung
# Als erstes werden beide Eingaben geprueft, ob es sich um korrekte Zahlen handelt
if(isNumber(eingabe1) and isNumber(eingabe2)):
    #In diesem Fall sind beides korrekte Zahlen und sie erwarten keine Probleme beim casten
    zahl1 = float(eingabe1)
    zahl2 = float(eingabe2)

    #Ausgabe je nach Fall
    if zahl1 == zahl2:
        print("Beide Zahlen sind gleichgross: ", zahl1)
    if zahl1 > zahl2:
        print(zahl1, " ist groesser als ", zahl2)
    if zahl1 < zahl2:
        print(zahl2, " ist groesser als ", zahl1)
else:
    #Ausgabe Fehlerfall
    print("Es gab ein Problem mit den Zahleingaben, es konnte keine Maximalzahl ermittelt werden.")
