
cityFile = open("Lecture5_NumpyMatplotScipy/ornek.txt")

cityArr = cityFile.read().split("\n")

cityDict = {}

for line in cityArr:
    info = line.split(",")
    cityName = info[0]
    day = int(info[1])
    rainfall = float(info[2])

    if cityName in cityDict.keys():
        days = cityDict[cityName]
        days[day] = rainfall
    else:
        cityDict[cityName] = {day: rainfall}

for name in cityDict.keys():
    min = 99999
    max = -9999
    sum = 0
    for value in cityDict[name].values():
        if value > max:
            max = value
        if value < min:
            min = value
        sum += value
    
    avg = sum / len(cityDict[name].values())
    print(f'{name}:\nmin: {min}\nmax: {max}\n average: {avg}')


