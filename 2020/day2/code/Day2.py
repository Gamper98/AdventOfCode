import re

def readIn(text, paswrd):
    with open(text, 'r') as f:
        for line in f.readlines():
            passwrd.append(re.findall(r'(\d+)-(\d+) (\w): (\w+)', line)[0])

def correctPasswrds(passwrd):
    correct = 0
    for line in passwrd:
        if int(line[0]) <= line[3].count(line[2]) <= int(line[1]):
            correct += 1
    return correct

def correctPasswrdsToboggan(passwrd):
    correct = 0
    for line in passwrd:
        if (line[3][int(line[0])-1] == line[2]) != (line[3][int(line[1])-1] == line[2]):
            correct += 1
    return correct

passwrd = []
readIn(r'2020\day2\input\input.txt',passwrd)
print(correctPasswrds(passwrd))
print(correctPasswrdsToboggan(passwrd))