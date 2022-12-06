"""
File Name: day04.py
Created Date: 12/04/2022
Author: Eduardo Estrada
Purpose:  
    --- Day 4: Camp Cleanup ---
    https://adventofcode.com/2022/day/4 
    --- Part One ---
    In how many assignment pairs does one range fully contain the other?
    --- Part Two ---
    In how many assignment pairs do the ranges overlap?
"""
 

def is_full_qualifed(item_1, item_2):

    count = 0
    if item_1.issubset(item_2) or item_2.issubset(item_1):
        count = 1

    return count

def is_over_lapping(item_1, item_2):
    
    found = 0
    if item_2.intersection(item_1): 
        found = 1

    return found

with open('input.txt', 'r', encoding="utf-8") as f:
    
    lines = f.readlines()
    answer1 = 0
    answer2 = 0
    for line in lines:
        
        # Split string into different variables instead of array in Python 
        assignments_a, assignments_b = line.strip().split(",")
        start1, stop1 = assignments_a.strip().split("-")
        start2, stop2 = assignments_b.strip().split("-")
        
        a = set(range(int(start1), int(stop1) + 1))
        b = set(range(int(start2), int(stop2) + 1))

        z = is_full_qualifed(a, b)
        w = is_over_lapping(a, b)
    
        answer1 += z
        answer2 += w

    print('Part 1 = {} Part 2 = {}'.format(answer1, answer2))
         

