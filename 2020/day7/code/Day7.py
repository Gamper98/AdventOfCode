import re

def readIn(text, bags):
    with open(text, 'r') as f:
        for line in f.readlines():
            key = re.findall(r'(\w+ \w+) bags ', line)
            bags[key[0]] = re.findall(r'(\d+) (\w+ \w+) bag', line)

def recursiveShinyGold(bags, bag, sgfit):
    for item in bags:
        for (_, cont) in bags[item]:
            if bag == cont:
                recursiveShinyGold(bags, item, sgfit)
                sgfit.add(item)

def recursiveBagsToPutIn(bags, bag):
    sum = 0
    for item in bags:
        if bag == item:
            for num, type in bags[item]:
                sum += int(num) * recursiveBagsToPutIn(bags, type)
                sum += int(num)
            return sum

bags = {}
readIn(r'2020\day7\input\input.txt', bags)
sgfit = set()
recursiveShinyGold(bags, 'shiny gold', sgfit)
print(len(sgfit))
print(recursiveBagsToPutIn(bags, 'shiny gold'))