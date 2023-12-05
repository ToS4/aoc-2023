with open('input.txt.txt') as file:

    lines = [line.strip() for line in file]

    sum = 0

    for card, info in enumerate(lines):

        info = info.split()
        info.pop(0)
        info.pop(0)

        winning_numbers = []
        game_numbers = []

        switch = False

        for number in info:
            if number == '|':
                switch = True
                continue

            if not switch:
                winning_numbers.append(int(number))
            else:
                game_numbers.append(int(number))

        winners = []

        for winning_number in winning_numbers:
            if winning_number in game_numbers:
                winners.append(winning_number)

        points = 0

        if len(winners) > 0:
            points = 1
            for i in range(len(winners)-1):
                points *= 2

        sum += points


    print(sum)
    