
def addF(i, opcode):
    opcode[opcode[i+3]] = opcode[opcode[i+1]] + opcode[opcode[i+2]]

def multF(i, opcode):
    opcode[opcode[i+3]] = opcode[opcode[i+1]] * opcode[opcode[i+2]]

option = {1: addF, 2: multF}

def subTask(noun, verb):
    with open(r"2019\input\input2.txt", "r") as f:
        opcode = [ int(x) for x in f.read().rstrip('\n').split(',')]
        opcode[1], opcode[2], i = noun, verb, 0
        while(opcode[i] != 99):
            option[opcode[i]](i, opcode)
            i += 4
        return opcode[0]

def taskA():
    print(subTask(12,2))

def taskB():
    noun, verb = 0, 0
    while noun < 100:
        while verb < 100:
            value = subTask(noun, verb)
            if value == 19690720:
                print(100 * noun + verb)
                return
            verb += 1
        verb = 0
        noun += 1


taskA()
taskB()

    