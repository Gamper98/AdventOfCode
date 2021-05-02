from collections import namedtuple

OpInfo = namedtuple('OpInfo', 'prec assoc')
L, R = 'Left Right'.split()

ops = {
    '*': OpInfo(prec=2, assoc=L),
    '+': OpInfo(prec=2, assoc=L),
}

def readIn(text, expressions):
    with open(text, 'r') as f:
        expressions[:] = f.read().rstrip('\n').split('\n')

def get_input(expression):
    tokens = []
    for char in expression:
         if char != ' ':
             tokens.append(char)
    return tokens

def shunting(tokens):
    table = []
    stack = []
    for token in tokens:
        if token in ops:
            prec, assoc = ops[token]
            if assoc == L:
                while len(stack) != 0 and stack[-1] != '(' and prec <= ops[stack[-1]][0]:
                    table.append(stack.pop())
                stack.append(token)
            else:
                while len(stack) != 0 and stack[-1] != '(' and prec < stack[-1][prec]:
                    table.append(stack.pop())
                stack.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack[-1][0] != '(':
                table.append(stack.pop())
            stack.pop()
        else: table.append(token)
    while len(stack) != 0:
        table.append(stack.pop())
    return table

def calcSum(table):
    stack = []
    for item in table:
        if item in ops:
            a = int(stack.pop())
            b = int(stack.pop())
            if item == '+':
                stack.append(a+b)
            elif item == '*':
                stack.append(a*b)
        else:
            stack.append(item)
    return stack.pop()

def p1(expressions):
    sums = 0
    for item in expressions:
        sums += calcSum(shunting(get_input(item)))
    print(sums)

def p2(expressions):
    ops['+'] = OpInfo(prec=2, assoc=L)
    sums = 0
    for item in expressions:
        sums += calcSum(shunting(get_input(item)))
    print(sums)

expressions = []
readIn(r'2020\day18\input\input.txt', expressions)
p1(expressions)
p2(expressions)