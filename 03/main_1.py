with open('input.txt') as file:

    lines = [list(line.strip()) for line in file]

    used_cells = []
    sum = 0

    for y_index, y in enumerate(lines):
        for x_index, x in enumerate(y):

            if not lines[y_index][x_index].isdigit():
                continue

            for i in (-1,0,1):
                for j in (-1,0,1):

                    new_y_index = (y_index + i) % len(lines)
                    new_x_index = (x_index + j) % len(lines[0])

                    new_value = lines[new_y_index][new_x_index]

                    if new_y_index < y_index + 2 and new_y_index > y_index - 2:
                        if new_x_index < x_index + 2 and new_x_index > x_index - 2:

                            if not new_value.isdigit() and new_value != '.':

                                x_index_start = x_index
                                x_index_end = x_index

                                while x_index_start > 0:
                                    x_index_start -= 1
                                    if not lines[y_index][x_index_start].isdigit():
                                        x_index_start += 1
                                        break
                                
                                while x_index_end < len(lines[0]):
                                    x_index_end += 1
                                    if not lines[y_index][x_index_end].isdigit():
                                        x_index_end -= 1
                                        break

                                value = lines[y_index][x_index_start:x_index_end + 1]
                                
                                allowed_number = True

                                for x_number_index in range(x_index_start, x_index_end):
                                    if (y_index, x_number_index) in used_cells:
                                        allowed_number = False

                                if allowed_number:
                                    sum += int(''.join(value))

                                for x_number_index in range(x_index_start, x_index_end):
                                    used_cells.append((y_index,x_number_index))

    print(sum)