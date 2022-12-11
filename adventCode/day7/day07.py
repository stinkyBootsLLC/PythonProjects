"""
    File Name: day07.py
    Created Date: 12/09/2022
    Author: Eduardo Estrada
    Purpose:  

    --- Day 7: No Space Left On Device ---
 
      
"""

 
def get_organized_drive(unorganized_drive):
    organized_drive = {}
    sum_of_all_files = 0
    for key, values in unorganized_drive.items():
        organized_drive[key] = []
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
                organized_drive[key].append(value[4:])
        
        organized_drive[key].append(sum_of_dir)
        sum_of_all_files += sum_of_dir

    organized_drive["total"] = []
    organized_drive["total"].append(sum_of_all_files)

    return organized_drive

 
def get_dir_total(dict, key):
    a = 0
    contents = dict[key]
    for x in contents:
        if isinstance(x, int):
            a += x
    return a


 

    # newDrive = {}
   
    # for key, content in dict.items():
    #     # print(content)
    #     for value in content:
            
    #         if isinstance(value, str):
    #             # then its a drive
    #             # find the drives content
    #             if value != '/':
    #                 print(value)

    #                 newDrive[value] = []
    #                 for x in dict[value]:
    #                     if isinstance(x, int):
    #                         newDrive[value].append(x)
                             

    # print(newDrive)         



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
             

    # determine the total size of each directory 
    drive = get_organized_drive(data)
    # # determine the total size of each directory
    print(data)
    print(drive) #organized by dir/
     
  
'''
    finalP1answer = 0
    for key, values in drive.items():

        k = key
        a = 0

        for value in values:
            
            if isinstance(value, str):
                # print(value)
                # get the sum for that dir
                # print()
                # print('dir: {} {}'.format(value, drive[value]))
                a += get_dir_total(drive, value)
            else:
                # total of files
                a += value
        
        # directories with a total size of at most 100000.
        if a <= 100000:
            finalP1answer += a
            print('dir: {} {}'.format(k, a))
    
    print(finalP1answer)

''' 
        
                
     




    # 
    # The total size of a directory is the sum of 
    # the sizes of the files it contains, directly or indirectly   
    # 
    # Find all of the directories with a total size of at most 100000. 
    # What is the sum of the total sizes of those directories?

        