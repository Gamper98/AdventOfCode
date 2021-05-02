def readIn(text, boarding):
    with open(text, 'r') as f:
        boarding[:] = [[x] for x in f.read().split('\n')]

def seatID(boarding):
    for item in boarding:
        start, end = 0, 127
        for i in range(len(item[0])-3):
            if item[0][i] == 'F':
                end -= (end-start)//2 + 1
            elif item[0][i] == 'B':
                start += (end-start)//2 + 1
        row = start
        start, end = 0, 7
        for i in range(len(item[0])-3, len(item[0])):
            if item[0][i] == 'R':
                start += (end-start)//2 + 1
            elif item[0][i] == 'L':
                end -= (end-start)//2 + 1
        item.append(row)
        item.append(start)
        item.append(row*8+start)
        
def findOurSeat(boarding):
    for i in range(len(boarding)-1):
        if boarding[i][1] == 0:
            continue
        if boarding[i+1][3] - boarding[i][3] == 2:
            return boarding[i][3]+1

boarding = []
readIn(r'2020\day5\input\input.txt', boarding)
seatID(boarding)
boarding.sort(key=lambda x:x[3])
print(boarding[-1][3])
print(findOurSeat(boarding))