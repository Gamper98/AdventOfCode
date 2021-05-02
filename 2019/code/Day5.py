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
        print(intcode[i+1])
    else:
        print(intcode[intcode[i+1]])
    return i+2

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

def subTask(input):
    with open(r"2019\input\input5.txt", "r") as f:
        intcode = [ int(x) for x in f.read().rstrip('\n').split(',')]
        i = opcode[3](input,0,intcode)
        #print(intcode[i]%10)
        while(intcode[i] != 99):
            #print(intcode[i]%10)
            i = opcode[intcode[i]%10](i, intcode)

def taskA():
    subTask(1)

def taskB():
    subTask(5)


taskA()
taskB()

    