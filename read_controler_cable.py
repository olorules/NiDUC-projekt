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