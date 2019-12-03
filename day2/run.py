

def runProblem1():
    runProgram(12,2)


def runProblem2():
    for noun in list(range(99)):
        for verb in list(range(99)):
            out = runProgram(noun,verb)
            if(out == 19690720):
                print(f"Noun={noun}")
                print(f"Verb={verb}")
                break
            else:
                print(f'Output={out} Moving on')


def runProgram(noun,verb):
    programIndex = 0
    with open('day2\\input.txt') as stream:
        for line in stream.readlines():
            codes = list(map(int,(line.rstrip().split(','))))
        
        codes[1] = noun
        codes[2] = verb

        killProc = False
        while programIndex < len(codes) or killProc:
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

        return codes[0]
    return -1
