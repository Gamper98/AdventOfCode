colorcode = []
numberOfDigits = []
image = []
def taskA(wide,tall):
    with open(r"2019\input\input8.txt", "r") as f:
        colorcode = [int(x) for x in str(f.readline())]
    fewest0 = 0
    for i in range(int(len(colorcode)/wide/tall)):
        numberOfDigits.append([0,0,0])
        for k in range(wide*tall):
            numberOfDigits[-1][colorcode[i * wide * tall + k]] += 1
        if numberOfDigits[fewest0][0] > numberOfDigits[i][0]:
            fewest0 = i
    print(numberOfDigits[fewest0][1] * numberOfDigits[fewest0][2])
    
def taskB(wide,tall):
    with open(r"2019\input\input8.txt", "r") as f:
        colorcode = [int(x) for x in str(f.readline())]
    image = [2 for j in range(wide*tall)]    
    for i in range(int(len(colorcode)/wide/tall)):
        for k in range(wide*tall):
            if colorcode[i * wide * tall + k] == 0 and image[k] == 2:
                image[k] = 0
            elif colorcode[i * wide * tall + k] == 1 and image[k] == 2:
                image[k] = 1    
    for i in range(tall):
        print(image[i*wide:i*wide+wide])
taskA(25, 6)
taskB(25, 6)
