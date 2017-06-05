def read_ram():
    file = open('RAM.txt')

    lines = []
    dictionary = dict()

    for line in file:
        line = line[:-1]
        lines.append(line)

    file.close()

    lines_count = len(lines)
    i = 0

    while i < lines_count:
        dictionary[lines[i]] = lines[i+1]
        i += 2

    return dictionary

def ram_menu():
    list = []
    i = 0
    for key, value in read_ram().items():
        print(f"{i}. {key}\nCena: {value} zl")
        list.append(key)
        i += 1
    x = input("Wybierz RAM: ")
    return list[int(x)]
