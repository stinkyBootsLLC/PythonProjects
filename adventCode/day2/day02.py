"""
File Name: day02.py
Created Date: 12/2/2022
Author: Eduardo Estrada
Purpose: Elf Rock Paper Scissors https://adventofcode.com/2022/day/2 
"""
def game(rps):
    # (1 for Rock, 2 for Paper, and 3 for Scissors) 
    myScore = 0
    # Rock defeats Scissors	AZ CX
    if rps == 'A Z':
        #elf wins
        myScore = 3
    elif rps == 'C X':
        # then my score is 1 + 6
        myScore = 7
    # Scissors defeats Paper CY	BZ
    elif rps == 'C Y':
        #elf wins
        myScore = 2
    elif rps == 'B Z':
        # then my score is 3 + 6
        myScore = 9
    # Paper defeats Rock BX	AY
    elif rps == 'B X':
        #elf wins
        myScore = 1
    elif rps == 'A Y':
        # then my score is 2 + 6
        myScore = 8
    else:
        # DRAW
        if rps == 'A X':
             # AX ROCK 1 + 3
            myScore = 4
        elif rps == 'B Y':
            # BY PAPER 2 + 3
            myScore = 5
        elif rps == 'C Z':
            # CZ SCISSORS 3 + 3
            myScore = 6

    return myScore


def encodedGame(rps):

    score = 0
    choices = rps.split(' ')
    elf = choices[0]
    mine = choices[1]
    # X means you need to lose, 
    if mine == 'X':
        if elf == 'A':
            score = game('A Z')
        elif elf == 'B':
            score = game('B X')
        elif elf == 'C':
            score = game('C Y')
    # Y means you need to end the round in a draw,  
    elif mine == 'Y':
        if elf == 'A':
            score = game('A X')
        elif elf == 'B':
            score = game('B Y')
        elif elf == 'C':
            score = game('C Z')
    # Z means you need to win.
    elif mine == 'Z':
        if elf == 'A':
            score = game('A Y')
        elif elf == 'B':
            score = game('B Z')
        elif elf == 'C':
            score = game('C X')
 
    return score

with open('input.txt', 'r', encoding="utf-8") as f:
    lines = f.readlines()
    total_score = 0
    encoded_total_score = 0
    for line in lines:
        # --- Part One ---
        round = game(line.strip())
        total_score += round
        # --- Part Two ---
        encoded_round = encodedGame(line.strip())
        encoded_total_score += encoded_round
    # What would your total score be if everything goes exactly 
    # according to your strategy guide? 
    # --- Part One ---
    print('My total score =', total_score)
    # --- Part Two ---
    print('My encoded total score =', encoded_total_score)