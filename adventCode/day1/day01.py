# 
"""
File Name: day01.py
Created Date: 12/1/2022
Author: Eduardo Estrada
Purpose: https://adventofcode.com/2022/day/1 
--- Day 1: Calorie Counting ---
(anonymous user #2449475)
--- Part One ---
Find the Elf carrying the most Calories. 
How many total Calories is that Elf carrying?
--- Part Two ---
Find the top three Elves carrying the most Calories. 
How many Calories are those Elves carrying in total?
"""

calories = [] # list of total calories for EACH elf

# This list represents the Calories of the food carried by Elves:
with open('calorieList.txt', 'r', encoding="utf-8") as f:
    lines = f.readlines()
    totalCals = 0 # for the sum of EACH elf

    for line in lines:
        # if line IS NOT empty
        if line.strip():
            # add the calories
            totalCals += int(line) #typecast to int
        else:
            # The line is empty and a new elf is next
            # append total caloried to calories list
            calories.append(totalCals)
            # reset
            totalCals = 0

    # --- Part One ---
    # Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?
    print("The", calories.index(max(calories)) + 1, "th elf is carrying ",max(calories), "calories") 
    
    # --- Part Two ---
    # Find the top three Elves carrying the most Calories. 

    # sort in reverse so the highest values are first in the list
    calories.sort(reverse=True)
    
    topThree = 0 # sum of top 3
    # loop thru the top 3
    for i in range(3):
        # add em up
        topThree += int(calories[i])
    # How many Calories are those Elves carrying in total?
    print("The total calories of the top three elves =",topThree)
 
     

