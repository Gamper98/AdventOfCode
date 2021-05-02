def taskA():
    sum = 0
    with open(r"2019\input\input1.txt", "r") as f:
        for line in f:
            sum += int(int(line) / 3) - 2
    print(sum)

def taskB():
    sum = 0
    with open(r"2019\input\input1.txt", "r") as f:
        for line in f:
            fuel = int(int(line) / 3) - 2
            sum += fuel
            while(fuel):
                fuel = int(fuel / 3) - 2
                if(fuel < 0):
                    fuel = 0
                sum += fuel
    print(sum)

taskA()
taskB()