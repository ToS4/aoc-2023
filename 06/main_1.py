times = []
distances = []

with open('input.txt') as file:

    lines = [line.strip() for line in file]

    for line in lines:
        line = line.split()

        for number in range(1,len(line)):
            if "Time" in line[0]:
                times.append(int(line[number]))
            elif "Distance" in line[0]:
                distances.append(int(line[number]))

results = []

for game in range(len(times)):
    time = times[game]
    distance = distances[game]
    counter = 0

    for hold_time in range(time):
        
        travel_distance = hold_time *  (time-hold_time)

        if travel_distance > distance:
            counter += 1

    results.append(counter)

result = 1

for x in results:
    result *= x  

print(result)