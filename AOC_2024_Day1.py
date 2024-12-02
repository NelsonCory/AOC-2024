#AOC-2024-Day 1
import fileinput

def loadData(leftArr,rightArr):

    for line in fileinput.input(files="fileinput.txt"):
        lineArr = line.split()
        leftArr.append(int(lineArr[0]))
        rightArr.append(int(lineArr[1]))
    leftArr.sort()
    rightArr.sort()

def part_1():
    sumDistances = 0
    leftArr = []
    rightArr = []
    loadData(leftArr,rightArr)
    for i in range(len(leftArr)):
        sumDistances += abs(leftArr[i] - rightArr[i])
    print(sumDistances)

def part_2():
    similarityScore = 0
    leftArr = []
    rightArr = []
    loadData(leftArr,rightArr)

    #prepare dictionary of {itemValue: numberOfInstances}
    thisdict = {rightArr[0]:0}
    for i in rightArr:
        if i in thisdict:
            thisdict.update({i : thisdict[i]+1})
        else:
            thisdict[i] = 1
    # calculate
    for i in leftArr:
        if i in thisdict:
            similarityScore += i * thisdict[i]
    print(similarityScore)
    
part_1()
part_2()
