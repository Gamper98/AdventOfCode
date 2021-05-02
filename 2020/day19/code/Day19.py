import itertools

def readIn(text, rule, validate):
    with open(text, 'r') as f:
        half1, half2 = f.read().rstrip('\n').split('\n\n')
        validate[:] = half2.split('\n')
        for row in half1.split('\n'):
            p, c = row.split(':')
            rule[int(p)] = [[]]
            for num in c.lstrip(' ').split(' '):
                if num == '|':
                    rule[int(p)].append([])
                    continue
                if num == '"a"' or num == '"b"':
                    rule[int(p)][:] = [[num[1]]]
                    continue
                rule[int(p)][-1].append(int(num))
        #print(rule)

def topological_order(rules):
    visited_nodes = []
    order = []

    def dfs(rules, node):
        visited_nodes.append(node)
        if node == 'a' or node == 'b':
            return
        rule = rules[node]
        for l in rule:
            for num in l:
                if num not in visited_nodes:
                    dfs(rules, num)
        order.append(node)

    dfs(rules, 0)
    #order.reverse()
    #order.append(0)
    ordering = {element: index for index, element in enumerate(order)}
    return order

def calcRules(ordering, rules, valid):
    subwords = []
    for item in ordering:
        #print('------')
        nextWord = rules.pop(item)
        #print(nextWord)
        subWords = [list(map(lambda x:''.join(x), list(itertools.product(*item)))) for item in nextWord]
        #print(subWords)
        subWords = list(itertools.chain.from_iterable(subWords))
        #print(subWords)
        #print('+++++++')
        for rule in rules.values():
            rule[:] = [[subWords if y == item else y for y in x] for x in rule]
            #print(rule)
    valid[:] = subWords

def validateWords(validate, valid):
    #print(set(valid))
    #print(set(validate))
    print(len(set(valid) & set(validate)))


#part1
""" 
rules, validate, valid = {} , [], []
readIn(r'2020\day19\input\input.txt', rules, validate)
ordering = topological_order(rules)
#print(ordering)
calcRules(ordering, rules, valid)
#print(valid)
validateWords(validate, valid) 
"""

#part2
""" 
def ValidateWord(rules, word, pos, startNode):
    for item in rules[startNode]:
        isGood = True
        if word[pos] == item:
            return (True, pos+1)
        for nextNode in item:            
            returnValue = ValidateWord(rules, word, pos, nextNode)
            isGood += returnValue[0]
            if isGood: pos = returnValue[1]
            if not isGood: return(False, pos)
        if isGood: return (True, pos)
"""  
        
def ValidateWord(rules, word, pos, currentNode):
    trueSides = []
    for item in rules[currentNode]:
        if item == word[pos]: 
            return (True, pos)
        for nextNode in item:
            returnValue = ValidateWord(rules, word, pos, nextNode)

        if("both side are True"): trueSides.append(("some pos Value"))

        




def checkValidWords(rules, validate):
    valid = 0
    for word in validate:
        if ValidateWord(rules, word, 0, 0):
            valid += 1
    print(valid)

rules, validate, valid = {} , [], []
readIn(r'2020\day19\input\input.txt', rules, validate)
rules[8] = [[42],[42,8]]
rules[11] = [[42,31],[42,11,31]]
print(rules)
checkValidWords(rules, validate)