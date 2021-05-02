from math import factorial
from random import randint
from copy import deepcopy
import queue

def paramdecoder(i, intcode):
    c, b = int(intcode[i]/100)%10, int(intcode[i]/1000)
    param1, param2 = 0, 0
    if c:
        param1 = intcode[i+1]
    else:
        param1 = intcode[intcode[i+1]]
    if b:
        param2 = intcode[i+2]
    else:
        param2 = intcode[intcode[i+2]]
    return (param1,param2)

def addF(i, intcode):
    params = paramdecoder(i, intcode)
    intcode[intcode[i+3]] = params[0] + params[1]
    return i+4

def multF(i, intcode):
    params = paramdecoder(i, intcode)
    intcode[intcode[i+3]] = params[0] * params[1]
    return i+4

def inputC(input,i,intcode):
    intcode[intcode[i+1]] = input
    return i+2

def outputC(i,intcode):
    if int(intcode[i]/100):
        return (i+2, intcode[i+1])
    else:
        return (i+2, intcode[intcode[i+1]])

def jumpifTrue(i, intcode):
    params = paramdecoder(i, intcode)
    if params[0]:
        return params[1]
    return i+3

def jumpifFalse(i, intcode):
    params = paramdecoder(i, intcode)
    if not params[0]:
        return params[1]
    return i+3

def lessThan(i, intcode):
    params = paramdecoder(i, intcode)
    if params[0] < params[1]:
        intcode[intcode[i+3]] = 1
    else:
        intcode[intcode[i+3]] = 0
    return i+4

def equals(i, intcode):
    params = paramdecoder(i, intcode)
    if params[0] == params[1]:
        intcode[intcode[i+3]] = 1
    else:
        intcode[intcode[i+3]] = 0
    return i+4

opcode = {1: addF, 2: multF, 3: inputC, 4: outputC, 5: jumpifTrue, 6: jumpifFalse, 7: lessThan, 8: equals}

def subTask(input, modeCode):
    output = []
    for i in range(len(input)):
        q = queue.Queue()
        q.put(input[i])
        output.append(q)
    output[0].put(0)
    intcode = []
    with open(r"2019\input\input7.txt", "r") as f:
        file = [ int(x) for x in f.read().rstrip('\n').split(',')]
        file.append(0)
        for i in range(len(output)):
            intcode.append(deepcopy(file))
        while True:
            for i in range(len(output)):                
                k = intcode[i][-1]
                while True:
                    if intcode[i][k]%100 == 3:
                        k = opcode[3](output[i].get(), k, intcode[i])
                        continue
                    elif intcode[i][k]%100 == 4:
                        k, tmp = opcode[4](k, intcode[i])
                        output[(i+1)%5].put(tmp)
                        break
                    elif intcode[i][k]%100 == 99:
                        if i == 4:
                            return output[0].get()
                        else:
                            break
                    k = opcode[intcode[i][k]%100](k, intcode[i])
                intcode[i][-1] = k

def recursiveGenerateSequences(seq, pos, end, start = 0):
    sequences = []
    for i in range(start, end+1):
        if i not in seq:
            seq[pos] = i
            if pos != 4:
                sequences += recursiveGenerateSequences(deepcopy(seq), pos+1, end, start)
            else:
                sequences.append(seq)
    return sequences

def recAmplyfContrModule(i, seq, input):
    if i != 0:
        input = recAmplyfContrModule(i-1, seq, input)
    output = subTask([seq[i], input], 1)
    return output[-1]

def taskA():
    sequences = recursiveGenerateSequences([-1,-1,-1,-1,-1], 0, 4)
    output = 0
    for seq in sequences:
        output = max(output, subTask(seq, 2))
    print(output)

def taskB():
    sequences = recursiveGenerateSequences([-1,-1,-1,-1,-1], 0, 9, 5)
    output = 0
    for seq in sequences:
        output = max(output, subTask(seq, 2))
    print(output)
    
#taskA()
taskB()
#print(subTask([9,8,7,6,5], 2))