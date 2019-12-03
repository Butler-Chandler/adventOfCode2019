

def runProblem1():
    commands = runProgram()


def runProgram():
    programIndex = 0
    with open('day2\\input.txt') as stream:
        for line in stream.readlines():
            codes = list(map(int,(line.rstrip().split(','))))

        killProc = False
        while programIndex < len(codes) or killProc:
            print(codes[programIndex])
            if codes[programIndex] == 1:
                indexToUpdate = codes[programIndex+3]
                codes[indexToUpdate] = codes[codes[programIndex+1]] + codes[codes[programIndex+2]]
                programIndex += 4

            elif codes[programIndex] == 2:
                indexToUpdate = codes[programIndex+3]
                codes[indexToUpdate] = codes[codes[programIndex+1]] * codes[codes[programIndex+2]]
                programIndex += 4

            elif codes[programIndex] == 99:
                killProc = True
                break   

        print(codes)
    return -1
