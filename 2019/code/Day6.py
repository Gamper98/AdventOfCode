input = []

def recursiveTreeConnections(i, parent, child):
    sum = i
    for Iparent,Ichild in input:
        if Iparent == child:
            sum += recursiveTreeConnections(i+1, child, Ichild)
    return sum

def recursiveTreeAtoB(parent, child):
    sum, a_found, b_found = 0, False, False
    for Iparent,Ichild in input:
        if Iparent == child and Ichild == "YOU":
            return (1, True, False)
        elif Iparent == child and Ichild == "SAN":
            return (1, False, True)
        elif Iparent == child:            
            output = recursiveTreeAtoB(child, Ichild)
            sum += output[0]
            a_found = a_found or output[1]
            b_found = b_found or output[2]
    if a_found and b_found:
        return (sum, True, True)
    elif not a_found and not b_found:
        return (0, False, False)
    elif b_found:
        return (sum+1, False, True)
    else:
        return (sum+1, True, False)

def taskA():
    with open(r"2019\input\input6.txt", "r") as f:
        for lines in f:
            input.append(lines.rstrip('\n').split(')'))
    print(recursiveTreeConnections(0, 0, "COM"))

def taskB():
    with open(r"2019\input\input6.txt", "r") as f:
        for lines in f:
            input.append(lines.rstrip('\n').split(')'))
    print(recursiveTreeAtoB(0, "COM")[0])

#taskA()
taskB()