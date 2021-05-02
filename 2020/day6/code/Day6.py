def clearGroupValues(group):
    group['personAns'] = []
    group['answered'] = set()
    group['everyoneYes'] = set()

def groupAppend(group, groups):
    group['everyoneYes'] = group['answered'].copy()
    for ans in group['personAns']:
        group['everyoneYes'] &= {x for x in ans}
    groups.append(group.copy())
    clearGroupValues(group)

def readIn(text, groups):
    with open(text, 'r') as f:
        group = {}
        clearGroupValues(group)
        for line in f.readlines():
            if line != '\n':                
                group['personAns'].append(line.rstrip('\n'))
                group['answered'] |= {x for x in line.rstrip('\n')}

            else:
                groupAppend(group, groups)
        groupAppend(group, groups)

groups = []
readIn(r'2020\day6\input\input.txt', groups)
ans = sum(len(x['answered']) for x in groups)
print(ans)
ans = sum(len(x['everyoneYes']) for x in groups)
print(ans)