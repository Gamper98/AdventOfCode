def readIn(text, commands):
    with open(text, 'r') as f:
        for line in f.readlines():
            t = line.rstrip('\n').split(' ')
            commands.append([t[0], int(t[1])])

def nop():
    return

def jmp():
    return

def acc():
    return

coms = { 'nop': nop, 'jmp': jmp, 'acc': acc}

def loopAccNum(commands):
    acc = 0
    i = 0
    visited = []
    while True:
        if i in visited or i >= len(commands):
            return acc, i
        else:
            visited.append(i)
        if commands[i][0] == 'acc':
            acc += commands[i][1]
        elif commands[i][0] == 'jmp':
            i += commands[i][1]
            continue
        i += 1

def changeCmd(i, commands):
        if commands[i][0] == 'jmp':
            commands[i][0] = 'nop'
        elif commands[i][0] == 'nop':
            commands[i][0] = 'jmp'

def findWorkingCommand(commands):
    for i in range(len(commands)):
        if commands[i][0] != 'nop' and commands[i][0] != 'jmp':
            continue
        changeCmd(i, commands)
        acc, ii = loopAccNum(commands)
        if ii >= len(commands):
            return(acc)
        changeCmd(i, commands)
        


commands = []
readIn(r'2020\day8\input\input.txt', commands)
print(loopAccNum(commands))
print(findWorkingCommand(commands))