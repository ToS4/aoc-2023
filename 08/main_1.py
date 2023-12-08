with open("input.txt") as file:
    lines = [line.strip() for line in file]

    instructions = lines[0]
    nodes = {}
    found = False

    current = ""
    steps = 0

    for index in range(2, len(lines)):

        line = lines[index]
        line = line.replace(",","")
        line = line.replace("(","")
        line = line.replace(")","")
        line = line.split()

        if index == 2:
            current = line[0] 

        nodes[line[0]] = {'L': line[2], 'R': line[3]}

    while not found:
        for instruction in instructions:
            
            if current == "ZZZ":
                found = True
                break

            current = nodes[current][instruction]

            steps += 1

    print(steps)