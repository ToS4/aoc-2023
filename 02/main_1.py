with open('input.txt') as file:

    lines = [line.strip() for line in file]

    sum = 0

    for id, line in enumerate(lines):

        info = line.split(";")

        game_possible = True

        for index, game in enumerate(info):
            game = game.split(":")

            if index == 0:
                game.pop(0)

            game = game[0].strip().split(",")

            for i,v in enumerate(game):
                game[i] = v.split()

            info[index] = game

        for pack in info:

            red_cubes = 12
            green_cubes = 13
            blue_cubes = 14

            for points, team in pack:

                if team == "red":
                    red_cubes -= int(points)
                if team == "green":
                    green_cubes -= int(points)
                if team == "blue":
                    blue_cubes -= int(points)

            if red_cubes < 0 or green_cubes < 0 or blue_cubes < 0:
                game_possible = False

        if game_possible:
            sum += (id + 1)

    print(sum)