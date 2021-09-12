"""
File: mycompareFiles.py
Created Date: 9/12/2021
Purpose: Compare two text files 
This solution reads both files in one pass, excludes blank lines, 
and prints COMMON lines regardless of their position in the file:
  
""" 
print("starting routine")
with open('outlook.txt', 'r') as file1:
    with open('intranet.txt', 'r') as file2:
        same = set(file1).intersection(file2)
        print("finished opening files")

same.discard('\n')

with open('output_file.txt', 'w') as file_out:
    for line in same:
        file_out.write(line)

print("routine complete")