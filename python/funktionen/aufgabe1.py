#!/usr/bin/python3

# Eingabe
eingabe_str = input("Bitte geben Sie eine Zahl ein: ")

# Verarbeitung
try:
    float(eingabe_str)
except:
    print("Es ist keine Zahl eingegeben worden")


# Ausgabe
print("Es wurde folgender Text eingegeben: " + eingabe_str)