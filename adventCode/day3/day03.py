"""
File Name: day03.py
Created Date: 12/3/2022
Author: Eduardo Estrada
Purpose: Day 3: Rucksack Reorganization 
https://adventofcode.com/2022/day/3 
"""
def findCommonChars(item_1, item_2, item_3=None):
    common_characters = ""
    comparment1 = set(item_1)
    comparment2 = set(item_2)
    common_characters += ''.join(sorted(comparment1.intersection(comparment2)))

    if item_3 is not None:
        items = [item_1,item_2,item_3]
        common_characters = set.intersection(*map(set,items))
    return common_characters


def findPriority(commonItems):
    PRIORITIES = ".abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return PRIORITIES.index(next(iter(commonItems)))


with open('input.txt', 'r', encoding="utf-8") as f:
    lines = f.readlines()
    first_comparment = []
    second_comparment = []
    common_item_types =[]
    sum_priorities = 0
    
    for line in lines:
        nAmount = len(line) - 1
        nHalf = int(nAmount / 2)
        common_item_types.append(findPriority(findCommonChars(line[0:nHalf], line[nHalf:-1])))
        sum_priorities += findPriority(findCommonChars(line[0:nHalf], line[nHalf:-1]))

    x = iter(lines)
    sum_priorities2 = 0 
    for a, b, c in zip(x, x, x):
        sum_priorities2 += findPriority( findCommonChars(a.strip(), b.strip(), c.strip()) )

    print("Part 1",sum_priorities)
    print("Part 2",sum_priorities2)
