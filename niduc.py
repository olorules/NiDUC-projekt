from read_ram import read_ram
from read_cpu import read_cpu
from read_drives import read_drives
from read_bbu import read_bbu
from read_network_card import read_network_card
from read_controler_cable import read_controler_cable

import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def cpu_menu():
    for key, value in read_cpu().items():
        print(f"{key}\nCena: {value} zl")

def menu():
    loop = True

    while loop:

        print("1.Procesory")
        print("2.RAM")
        print("3.Dyski")
        print("4.BBU")
        print("5.Karty sieciowe")
        print("6.Kontroler sprzętowy")

        usr_input = input("Podaj opcje: ")

        if usr_input == "1":
            cls()
            cpu_menu()
            print()
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




configuration = {"CPU": None, "RAM": None, "Drives": None, "BBU": None, "Network Card": None, "Controler cable": None}

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
