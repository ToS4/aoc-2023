with open('input.txt') as file:

    lines = [line.strip() for line in file]

    sum = 0

    for id, line in enumerate(lines):

        info = line.split(";")

        red_cubes = 1
        green_cubes = 1
        blue_cubes = 1

        for index, game in enumerate(info):
            game = game.split(":")

            if index == 0:
                game.pop(0)

            game = game[0].strip().split(",")

            for i,v in enumerate(game):
                game[i] = v.split()

            info[index] = game

        for pack in info:

            for points, team in pack:

                if team == "red":
                    if int(points) > red_cubes:
                        red_cubes = int(points)
                if team == "green":
                    if int(points) > green_cubes:
                        green_cubes = int(points)
                if team == "blue":
                    if int(points) > blue_cubes:
                        blue_cubes = int(points)

        sum += red_cubes * green_cubes * blue_cubes

    print(sum)