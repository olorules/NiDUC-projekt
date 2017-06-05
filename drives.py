def read_drives():
    file = open('Dyski.txt')

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
        dictionary[lines[i]].append(lines[i+2])
        i += 3

    return dictionary

def drives_menu():
    list = []
    i = 0
    for key, value in read_drives().items():
        print(f"{i}. {key}\nCena: {value} zl")
        list.append(key)
        i += 1
    x = input("Wybierz Dyski: ")
    return list[int(x)]
