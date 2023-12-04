with open('input.txt') as file:

    lines = [line.strip() for line in file]

    coppies = {}

    for card, given_info in enumerate(lines):

        dict_index = str(card)

        if not dict_index in coppies:
            coppies[dict_index] = 1
        else:
            coppies[dict_index] += 1

        if dict_index in coppies:
           for i in range(coppies[dict_index] ):

            info = given_info.split()
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

            for i in range(len(winners)):

                index = str(card+i+1)

                if index in coppies:
                    coppies[index] += 1
                else:
                    coppies[index] = 1

    sum = 0
    for i in coppies:
        sum += coppies[i]

    print(sum)