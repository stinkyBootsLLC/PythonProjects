"""
    File Name: day06.py
    Created Date: 12/08/2022
    Author: Eduardo Estrada
    Purpose:  
        --- Day 6: Tuning Trouble ---
        https://adventofcode.com/2022/day/6
        --- Part One ---
        start_of_packet_marker  
        --- Part Two ---
        start_of_message_marker
"""

def get_marker(datastream, amount_of_diff_chars):

    marker = 0 
    pointer = 0

    while True:
        packet = datastream[pointer:(pointer + amount_of_diff_chars)]
            
        has_repeated_chars = len(set(packet)) != len(packet)
        if not has_repeated_chars:
            marker = (pointer + amount_of_diff_chars)
            break

        pointer += 1

    return marker

with open('input.txt', 'r', encoding="utf-8") as f:

    lines = f.readlines()
    
    # parse input file
    for line in lines:

        start_of_packet_marker = get_marker(line, 4)
        print(start_of_packet_marker)

        start_of_message_marker = get_marker(line, 14)
        print(start_of_message_marker)