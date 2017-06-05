def read_controler_cable():
    file = open('Kontroler sprzętowy+kabel.txt')

    lines = []
    dictionary = dict()

    for line in file:
        line = line[:-1]
        lines.append(line)

    file.close()

    lines_count = len(lines)
    i = 0

    while i < lines_count:
        dictionary[lines[i]] = [lines[i+1]]
        i += 2

    return dictionary

def controler_cable_menu():
    list = []
    i = 0
    for key, value in read_controler_cable().items():
        print(f"{i}. {key}\nCena: {value} zl")
        list.append(key)
        i += 1
    x = input("Wybierz kontroler i kabel: ")
    return list[int(x)]
