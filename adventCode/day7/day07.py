"""
    File Name: day07.py
    Created Date: 12/09/2022
    Author: Eduardo Estrada
    Purpose:  

    --- Day 7: No Space Left On Device ---
 
      
"""
def get_dir_total(dict, key):
    a = 0
    contents = dict[key]
    for x in contents:
        if isinstance(x, int):
            a += x
    return a


def get_values(dict, key):
    return dict.get(key)
 
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
                organized_drive[key].append(value)
        
        organized_drive[key].append(sum_of_dir)
        sum_of_all_files += sum_of_dir

    organized_drive["total"] = []
    organized_drive["total"].append(sum_of_all_files)

    # add all the sizes for each directory
    for key, directory in organized_drive.items():
        for value in directory:
            if isinstance(value, str):
                if "dir" in value:
                    x = get_values(organized_drive, value)
                    for a in x:
                        if isinstance(a, int):
                            organized_drive[key].append(a)

    # remove all strings and just leave integers
    for key, directory in organized_drive.items():
        organized_drive[key] = [x for x in directory if not isinstance(x, str)]

    # return a dictionary of lists 
    # each list will have size value. either a dir or a file, doesn't matter 
    # ie. 'dir a' [size, size, size....]
    return organized_drive
# get the puzzle input
with open('input.txt', 'r', encoding="utf-8") as f:

    data = {}
   
    lines = f.readlines()
    # parse input file
    for line in lines:
        if "$ cd .." not in line.strip():
            if "$ cd" in line.strip():  
                location = "dir " + line[5:].strip()
                data[location] = []
            if "$" not in line.strip():
                data[location].append(line.strip())
          
    # determine the total size of each directory 
    drive = get_organized_drive(data)
    # # determine the total size of each directory
    # print(data)
    '''
    {
        'dir /': [23352670, 94269, 24933642], 
        'dir a': [94269, 584], 
        'dir e': [584], 
        'dir d': [24933642], 
        'total': [48381165]
    }
    '''
    print(drive)

 

 
  
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

        