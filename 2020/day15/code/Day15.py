def readIn(text, num):
    with open(text, 'r') as f:
        num[:] = [int(x) for x in f.read().rstrip('\n').split(',')]

def sumGame(num):
    turn = 1
    lastSpoken = num[-1]
    spokenNums = {}
    for item in num:
        spokenNums[item] = turn
        turn += 1
    print(spokenNums)
    while turn <= 30000000: 
        if lastSpoken in spokenNums.keys() and spokenNums[lastSpoken] != turn-1:
            lastSpokenBefore = turn-1 - spokenNums[lastSpoken]
            spokenNums[lastSpoken] = turn-1
            lastSpoken = lastSpokenBefore
        else:
            spokenNums[lastSpoken] = turn-1
            lastSpoken = 0
        turn += 1
        #print(spokenNums)
    print(lastSpoken)

num = []
readIn(r'2020\day15\input\input.txt', num)
sumGame(num)