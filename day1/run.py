def runProblem1():
    runningTotal = 0
    with open('day1\\input.txt') as data:
        for line in data.readlines():
            mass = int(line.rstrip())
            fuel = (mass//3 - 2)
            runningTotal += fuel
        print(runningTotal)


def runProblem2():
    runningTotal = 0
    with open('day1\\input.txt') as data:
        for line in data.readlines():
            mass = int(line.rstrip())
            fuel = determineFuel(mass)
            runningTotal += fuel
        print(runningTotal)


## 1969 requires 966
def determineFuel(mass):
    if (mass//3 - 2) < 0:
        return 0
    else:
        return (mass//3 - 2) + determineFuel((mass//3 - 2))