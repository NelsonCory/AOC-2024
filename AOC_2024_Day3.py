#AOC Day 3

import fileinput
import re

def loadData():
    with open('fileinput.txt', 'r') as file:
        content = file.read()
    return content


def part_1():
    data = loadData()
    mulRegex = "(mul\(\d+,\d+\))"
    mulList = re.findall(mulRegex,data)
    #print(mulList)
    multSum = 0

    #identify numbers, then multiply together and add to multSum
    for i in mulList:
        temp = i[4:-1].split(",")
        multSum += int(temp[0]) * int(temp[1])
    print(multSum)

part_1() # 153469856
