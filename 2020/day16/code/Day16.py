from copy import deepcopy
import re
import math

def readIn(text, fields, validNums, myTicket, OtherTickets):
    with open(text, 'r') as f:
        items = f.read().split('\n\n')
        for item in re.findall(r'([a-z ]+): (\d+)-(\d+) or (\d+)-(\d+)', items[0]):
            fields[item[0]] = [(int(item[1]),int(item[2])),(int(item[3]),int(item[4]))]
        for (start, end) in re.findall(r'(\d+)-(\d+)', items[0]):
            validNums.update(validNums | {i for i in range(int(start), int(end)+1)})
        myTicket[:] = [int(i) for i in (items[1].split('\n')[1]).split(',')]
        tickets = items[2].split('\n')[1:]
        OtherTickets[:] = [[int(x) for x in ticket.split(',')] for ticket in tickets]

def findInvalidTickets(validNums, OtherTickets, validTickets):
    sums = 0
    for ticket in OtherTickets:
        isValid = True
        for i in ticket:
            if i not in validNums:
                sums += i
                isValid = False
                break
        if isValid:
            validTickets.append(ticket)            
    print(sums)

def findDepartureNumber(fields, myTicket, validTickets):
    product = []
    validkeys = []
    print(myTicket)
    for key, ((start1, end1), (start2, end2)) in fields.items():
        print(key)
        validkeys.append([])
        for i in range(len(validTickets[0])):
            if i not in validkeys:
                validKey = True
                for ticket in validTickets:
                    if not (start1 <= ticket[i] <= end1 or start2 <= ticket[i] <= end2):
                        validKey = False
                        break
                if validKey:
                    validkeys[-1].append(i)
    validkeysSorted = deepcopy(validkeys)
    validkeysSorted.sort(key=lambda x:len(x))
    print(validkeys)
    print(validkeysSorted)
    for i in range(len(validkeys)):
        item = (validkeysSorted.pop(0)).pop(0)
        for i in range(len(validkeysSorted)):
            validkeysSorted[i].remove(item)
        for i in range(len(validkeys)):
            if len(validkeys[i]) != 1:
                validkeys[i].remove(item)
    product = [myTicket[validkeys[i][0]] for i in range(6)]
    print(math.prod(product))

fields, validNums, myTicket, OtherTickets, validTickets = {}, set(), [], [], []
readIn(r'2020\day16\input\input.txt', fields, validNums, myTicket, OtherTickets)
findInvalidTickets(validNums, OtherTickets, validTickets)
findDepartureNumber(fields, myTicket, validTickets)