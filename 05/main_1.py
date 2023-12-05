with open('input.txt') as file:

    lines = [line.strip() for line in file]

    seeds = []
    maps = {}
    currentMap = ""

    for line in lines:
        if line[:5] == "seeds":
            line = line.split()
            for index in range(1, len(line)):
                seeds.append(int(line[index]))
        elif "map" in line:
            line = line.split()

            currentMap = line[0]
            maps[currentMap] = []
        elif line != "":
            line = line.split()
            temp = []
            for number in line:
                temp.append(int(number))
            maps[currentMap].append(temp)

    location = float('inf')

    for seed in seeds:
        value = seed
        for map in maps:
            for element in maps[map]:

                destinationRangeStart, sourceRangeStart, rangeLength = element

                if value >= sourceRangeStart and value < sourceRangeStart + rangeLength:
                    offset = value - sourceRangeStart
                    value = destinationRangeStart + offset
                    break

        if value < location:
            location = value

    print(location)

    