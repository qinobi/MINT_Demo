#!/usr/bin/python3

# Initialisierung
nummernListe = [] # Leere Nummernliste zum Auffuellen

# Funktionen:
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

# Diese Funktion erwartet zwei Zahlen und gibt als Rueckgabewert die groessere der Beiden zurueck
# Sind Beide Zahlen gleich gross wird der Benutzer informiert und Zahl1 wird zurueckgegeben
def max_of_two_numbers(number1, number2):
    if number1 == number2:
        print("Beide Zahlen sind gleichgross.")
        return number1
    if number1 > number2:
        return number1
    if number1 < number2:
        return number2

# Eingabe
print("Geben Sie Zahlen mit Kommas getrennt ein.")
print("Beispiel: 3,5,6,7,18")
eingabe = input()

# Verarbeitung
# Aus der Eingabe wird eine Liste erstellt mit Kommas getrennt
stringListe = eingabe.split(",")

# Es werden nur korrekte Nummern in die Nummerliste aufgenommen
for string in stringListe:
    if isNumber(string):
        nummer = float(string)
        nummernListe.append(nummer)
    else:
        continue

# Nur wenn die Nummernliste etwas drin hat soll Code ausgefuehrt werden.
if len(nummernListe) > 0:
    max_in_list = nummernListe[0]
    # Nur Wenn die Nummerliste mind. 2 ELemente hat soll eine Schleife erstellt werden
    if len(nummernListe) > 1:
        for i in range(1,len(nummernListe)):
            max_in_list = max_of_two_numbers(max_in_list, nummernListe[i])
    # Ausgabe
    print(max_in_list, "wurde als groesste Zahl in der Liste ermittelt.")

else:
    # Ausgabe im Fehlerfall
    print("Es konnte kein Maximum ermittelt werden.")

