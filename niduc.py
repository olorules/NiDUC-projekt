from ram import ram_menu
from cpu import cpu_menu
from drives import drives_menu
from bbu import bbu_menu
from network_card import network_card_menu
from controler_cable import controler_cable_menu

import os

configuration = {"CPU": None, "RAM": None, "Drives": None, "BBU": None, "Network Card": None, "Controler cable": None}

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def menu():
    loop = True

    while loop:

        print("1.Procesory")
        print("2.RAM")
        print("3.Dyski")
        print("4.BBU")
        print("5.Karty sieciowe")
        print("6.Kontroler sprzętowy")
        print("7.Wypisanie aktualnej konfiguracji")

        usr_input = input("Podaj opcje: ")

        if usr_input == "1":
            cls()
            configuration["CPU"] = cpu_menu()
            print()
        elif usr_input == "2":
            cls()
            configuration["RAM"] = ram_menu()
            print()
        elif usr_input == "3":
            cls()
            configuration["Drives"] = drives_menu()
            print()
        elif usr_input == "4":
            cls()
            configuration["BBU"] = bbu_menu()
            print()
        elif usr_input == "5":
            cls()
            configuration["Network Card"] = network_card_menu()
            print()
        elif usr_input == "6":
            cls()
            configuration["Controler cable"] = controler_cable_menu()
            print()
        elif usr_input == "7":
            cls()
            for k, v in configuration.items():
                print(f"{k}: {v}")
        elif usr_input == "0":
            loop = False
        else:
            print("Wybrano złą opcję.")



cls()
print("\nElo, wybierz jaką chcesz konfigurację sprzętu.")
menu()
"""
loop = True

while loop:
    menu()
    usr_input = input("Podaj opcje: ")
    if usr_input == "1":
        print("CPU")
    elif usr_input == "2":
        print("RAM")
    elif usr_input == "3":
        print("DRIVE")
    elif usr_input == "4":
        print("BBU")
    elif usr_input == "5":
        print("NCARD")
    elif usr_input == "0":
        loop = False
    else:
        print("Wybrano złą opcję.")
"""
