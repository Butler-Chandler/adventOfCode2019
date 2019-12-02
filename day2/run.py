

def runProblem1():
    commands = parseOpCodes()


def parseOpCodes():
    program = {}
    procIndex = 0
    programIndex = 0
    codes = []
    with open('day2\\input.txt') as stream:
        for line in stream.readlines():
            codes = (line.rstrip().split(','))

        for code in codes:
            if(int(code) == 1):
                ## add op code
                print()
            if(code ==','):
                ## new index 
                print()

            #program.append(byte)

        print(program)
    return -1
