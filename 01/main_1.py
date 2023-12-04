with open('input.txt') as file:

    sum = 0

    for line in file:
        first = ""
        second = ""
        for char in line:
            if char.isdigit():
                if first  == "":
                    first = char
                    second = char
                else:
                    second = char

        sum += int(first+second)

    print(sum)