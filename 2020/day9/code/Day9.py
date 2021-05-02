
def readIn(text, nums):
    with open(text, 'r') as f:
        nums[:] = [int(x) for x in f.read().rstrip('\n').split('\n')]

def createPreamble(preamble , nums):
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            preamble.append(nums[i]+nums[j])

def changePreamble(preamble, nums):
    for i in range(1, len(nums)-1):
        preamble.remove(nums[i] + nums[0])
    for i in range(1, len(nums)-1):
        preamble.append(nums[i] + nums[-1])

def findFristOddOneOut(preamble, nums, preambleL):
    for i in range(preambleL, len(nums)):
        if nums[i] in preamble:
            changePreamble(preamble, nums[i-preambleL:i+1])
        else: 
            return nums[i], i

def findContiguousSet(nums, OddOne):
    for i in range(2, len(nums)):
        for j in range(len(nums)-i):
            if sum(nums[j:j+i]) == OddOne:
                return min(nums[j:j+i]) + max(nums[j:j+i])

nums = []
preamble = []
preambleL = 25
readIn(r'2020\day9\input\input.txt', nums)
createPreamble(preamble, nums[:preambleL])
oddOne, i = findFristOddOneOut(preamble, nums, preambleL)
sum = findContiguousSet(nums[:i], oddOne)
print(oddOne)
print(i)
print(sum)