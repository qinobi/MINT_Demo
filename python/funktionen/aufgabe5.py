#!/usr/bin/python3

# Eingabe
print("Geben Sie Zahlen mit Kommas getrennt ein.")
print("Beispiel: 3,5,6,7,18")
eingabe = input()

# Verabeitung
stringListe = eingabe.split(",")

# Ausgabe
print(stringListe)