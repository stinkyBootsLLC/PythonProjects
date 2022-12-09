"""
    File Name: day07.py
    Created Date: 12/09/2022
    Author: Eduardo Estrada
    Purpose:  

    --- Day 7: No Space Left On Device ---
 
      
"""
 

with open('input.txt', 'r', encoding="utf-8") as f:
    data = {}
   
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
             
        
            


    print(data)
    # determine the total size of each directory 
    # 
    # The total size of a directory is the sum of 
    # the sizes of the files it contains, directly or indirectly   
    # 
    # Find all of the directories with a total size of at most 100000. 
    # What is the sum of the total sizes of those directories?

        