from random import randint

def isValid(digits):
    isDoubleDigits = False
    for i in range(5):
        if digits[i+1] < digits[i]:
            return False
        if digits[i] == digits[i+1]:
            isDoubleDigits = True
    return isDoubleDigits 

def isDecreasing(digits):
    for i in range(5):
        if digits[i+1] < digits[i]:
            return True
    return False

def isInSingleDoubleDigit(digits):
    isDoubleDigits, isSingledoubleDigits = False, False
    for i in range(5):
        if digits[i] == digits[i+1] and not( isDoubleDigits or isSingledoubleDigits):
            isDoubleDigits = True
            isSingledoubleDigits = True
        elif digits[i] == digits[i+1] and isDoubleDigits and isSingledoubleDigits:
            isSingledoubleDigits = False
        elif digits[i] != digits[i+1] and not isSingledoubleDigits and isDoubleDigits:
            isDoubleDigits = False
        elif digits[i] != digits[i+1] and isSingledoubleDigits and isDoubleDigits:
            return True
    return isSingledoubleDigits 

valid = []
def taskA():
    first, last, count = 367479, 893698, 0
    for number in range(first, last+1):
        digits = [ int(digit) for digit in str(number)]
        if isValid(digits):
            count += 1
            valid.append(number)
    print(count)

def taskB():
    count, valid2 =  0, []
    for number in valid:
        digits = [ int(digit) for digit in str(number)]
        if (not isDecreasing(digits)) and isInSingleDoubleDigit(digits):
            count += 1
            valid2.append(number)
    print(count)
    #print(valid2)

taskA()
taskB()
