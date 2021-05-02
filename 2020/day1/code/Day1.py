def readIn(text, expense):
    with open(text, 'r') as f:
        for line in f.readlines():
            expense.append(int(line.rstrip('\n')))

def sumTwoTo2020(expense):
    expense.sort(reverse = True)
    for i in range(len(expense)):
        for j in range(-1, -(len(expense)-i), -1):
            if expense[i] + expense[j] == 2020:
                return expense[i] * expense[j]
            elif expense[i] + expense[j] >= 2020:
                break

def sumThreeTo2020(expense):
    for i in range(len(expense)):
        for j in range(-1, -(len(expense)-i), -1):
            if expense[i] + expense[j] > 2020:
                break
            for k in range(-1, j, -1):
                if expense[i] + expense[j] + expense[k] == 2020:
                    return expense[i] * expense[j] * expense[k]
                elif expense[i] + expense[j] + expense[k] > 2020:
                    break

#part 1
expense = []
readIn(r"2020\day1\input\input.txt",expense)
print(sumTwoTo2020(expense))

#part 2
print(sumThreeTo2020(expense))