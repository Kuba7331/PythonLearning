import math
import random


def binary_search(group, numToFind):
    begin_index = 0
    end_index = len(group) - 1

    while begin_index <= end_index:
        midpoint = begin_index + (end_index - begin_index) // 2
        midpoint_value = group[midpoint]
        if midpoint_value == numToFind:
            return midpoint
        elif numToFind < midpoint_value:
            end_index = midpoint - 1
        else:
            begin_index = midpoint + 1
    return None



randList = []
for x in range(0,100):
    randList.append(random.randint(1,100))
randList.sort()
for i in randList:
    print(i, end=" ")
number = int(input() + "\n")
print("Your number is at "+  str(binary_search(randList, number) + 1) + " position!")