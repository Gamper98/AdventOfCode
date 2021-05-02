import re

def readIn(text, passports):
    with open(text, 'r') as f:
        passp = {}
        for line in f.readlines():
            if line != '\n':
                items = re.findall(r'(\w+):(\W?\w+)', line.rstrip('\n'))
                for key, value in items:
                    passp[key] = value
            else:
                passports.append(passp.copy())
                passp.clear()
        passports.append(passp.copy())

def checkPass(passports):
    valid = 0
    vldecl = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    for item in passports:
        if len(item) == 8 or (len(item) == 7 and 'cid' not in item.keys()):
            if 1920 <= int(item['byr']) <= 2002 and 2010 <= int(item['iyr']) <= 2020 and 2020 <= int(item['eyr']) <= 2030:
                if (item['hgt'][-2:] == 'cm' and 150 <= int(item['hgt'][:-2]) <= 193) or (item['hgt'][-2:] == 'in' and 59 <= int(item['hgt'][:-2]) <= 76):
                    if re.match(r'#[0-9a-f]{6,6}', item['hcl']) != None:
                        if item['ecl'] in vldecl:
                            if len(item['pid']) == 9:
                                valid += 1
    return valid

passports = []
readIn(r'2020\day4\input\input.txt', passports)
print(checkPass(passports))
