#!/usr/bin/python3
print("Dez -> Bin")
eingabe = input("Geben Sie eine Zahl ein: ")
print("Es wurde folgende Zahl eingegeben: ", eingabe)

zahl = int(eingabe)

while (zahl > 0):
    rest = zahl % 2
    print(rest)
    zahl //= 2

print("Zahl von Unten nach Oben lesen")