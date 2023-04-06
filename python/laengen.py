#!/usr/bin/python3

def calculate():
    print("Längenrechner")

    def mm2cm(wert):
        return wert / 10

    def mm2dm(wert):
        return wert / 100

    def mm2m(wert):
        return wert / 1000

    def mm2km(wert):
        return wert / 1000000

    def cm2mm(wert):
        return wert * 10

    def dm2mm(wert):
        return wert * 100

    def m2mm(wert):
        return wert * 1000

    def km2mm(wert):
        return wert * 1000000

    def calculate_all_from_mm(mm):
        print(mm, "mm")
        print(mm2cm(mm), "cm")
        print(mm2dm(mm), "dm")
        print(mm2m(mm), "m")
        print('{0:f}'.format(mm2km(mm)), "km")


    running = True
    while (running):
        startWert = input("Geben Sie eine Zahl ein (ohne Einheit): ")
        startEinheit = input("Geben Sie die Einheit an: ").casefold()

        startWert = float(startWert)

        match startEinheit:
            case "mm":
                calculate_all_from_mm(startWert)

            case "cm":
                calculate_all_from_mm(cm2mm(startWert))

            case "dm":
                calculate_all_from_mm(dm2mm(startWert))

            case "m":
                calculate_all_from_mm(m2mm(startWert))

            case "km":
                calculate_all_from_mm(km2mm(startWert))

            case _:
                print("Keine gültige Einheit")
                exit(-1)

        repeat = input("Nochmals? (y/n): ")
        if repeat.casefold() != "y":
            running = False

