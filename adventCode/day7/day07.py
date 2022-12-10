"""
    File Name: day07.py
    Created Date: 12/09/2022
    Author: Eduardo Estrada
    Purpose:  

    --- Day 7: No Space Left On Device ---
 
      
"""
import re

with open('input.txt', 'r', encoding="utf-8") as f:
    data = {}
    drive = {}
    sum_of_all_files = 0
   
    lines = f.readlines()
    # parse input file
    for line in lines:
        
        if "$ cd" in line.strip():

            if "$ cd .." not in line.strip():  
                location = line[5:].strip()
                # print(location)
                data[location] = []

        if "$ ls" not in line.strip(): 
            if "$ cd " not in line.strip():
                # print(line.strip())
                data[location].append(line.strip())
             
    # determine the total size of each directory 
    for key, values in data.items():

        drive[key] = []
        sum_of_dir = 0

        for value in values:
            
            found_file = any(char.isdigit() for char in value)
            # found a file
            if found_file:
                # then get the size and name
                size, name = value.split(" ")
                sum_of_dir += int(size)
                
            else:
            # else its a directory
                # print(key + value[-1])
                drive[key].append(value[-1])
        
        drive[key].append(sum_of_dir)
        sum_of_all_files += sum_of_dir
        
    
    
    # determine the total size of each directory
    print(data)
    print(drive)
    print(sum_of_all_files)
        
                
     




    # 
    # The total size of a directory is the sum of 
    # the sizes of the files it contains, directly or indirectly   
    # 
    # Find all of the directories with a total size of at most 100000. 
    # What is the sum of the total sizes of those directories?

        