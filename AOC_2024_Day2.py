#AOC Day 2

import fileinput

def loadData():
    data = []
    for line in fileinput.input(files="fileinput.txt"):
        lineArr = line.split()
        report = []
        for i in lineArr:
            report.append(int(i))
        data.append(report)
    return data


def part_1():
    numSafe = 0
    data = loadData()
    for i in data:
        numSafe += determineSafety(i)
    print(numSafe)

def determineSafety(row):
    if row[0] <  row[1]:
        rowType = "increasing"
    else:
        rowType = "decreasing"
        
    for i in range(len(row) - 1):
        
        if rowType == "increasing":
            if row[i] >= row[i+1] or abs(row[i] - row[i+1]) > 3:
                return 0
        else:
            if row[i] <= row[i+1] or abs(row[i] - row[i+1]) > 3:
                return 0
    return 1
        
def determineRowType(row,curr):
    if row[curr] < row[curr+1]:
        return "increasing"
    else:
        return "decreasing"

def determineSafety_dampener(row):
    if row[0] <  row[1]:
        rowType = "increasing"
    else:
        rowType = "decreasing"
        
    for i in range(len(row) - 1):
        
        if rowType == "increasing":
            if row[i] >= row[i+1] or abs(row[i] - row[i+1]) > 3:
                return 0
        else:
            if row[i] <= row[i+1] or abs(row[i] - row[i+1]) > 3:
                return 0
    return 1


def part_2():
    numSafe = 0
    data = loadData()
    numSafe += determineSafety_dampener(data[0])
    #for i in data:
    #    numSafe += determineSafety_dampener(i)
    print(numSafe)
    
part_1() #390
part_2()
