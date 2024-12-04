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
    print(mulList)


part_1()
