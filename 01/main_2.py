

with open('input.txt') as file:

    lines = [line.strip() for line in file]

    spelled_out_numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    sum = 0

    for line in lines:

        first = ""
        second = ""

        string = ""
        
        for char in line:

            if first != "":
                string = ""
                break

            if char.isdigit():
                string = ""
                first = char
                break

            string += char

            for i, spelled_out_number in enumerate(spelled_out_numbers):
                if spelled_out_number in string:
                    if first == "":
                        first = str(i + 1)

        string = ""

        for char in line[::-1]:
            
            if second != "":
                string = ""
                break

            if char.isdigit():
                string = ""
                second = char
                break

            string += char

            for i, spelled_out_number in enumerate(spelled_out_numbers):
                if spelled_out_number in string[::-1]:
                    if second == "":
                        second = str(i + 1)

        sum += int(first + second)

    print(sum)