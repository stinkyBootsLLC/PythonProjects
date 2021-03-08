"""
FileName: newCourse.py
Created: 3/8/2021
Author: Eduardo Estrada
Purpose:
create a simple script to make new course structure for 
myself when I take a new course.
i.e.
current directory 

CMSC405
    WEEK1
    ....READ
    ....ASSIGNMENTS
    ....LAB
    ....DISCUSSIONS
            disscusion_1.docx
    WEEK2
    .
    . to
    .
    WEEK8

the course name will be a user input
"""
import os

# the current folder this file is in
parent_folder  = os.path.dirname(os.path.realpath(__file__))
print(parent_folder)
courseName = input("Enter course name").upper()
# make the new directory
os.makedirs("{}/{}".format(parent_folder,courseName))
# change to the new directory 
os.chdir("{}/{}".format(parent_folder,courseName))
# get the current working directory
# should be the root where this file is located /  
# then the input folder name
# (rootfolder/nameInput)
course_root_folder = os.getcwd()
# loop 8 times for 8 folders
for i in range(8):
    os.makedirs('week{}'.format(i + 1))
    week = 'week{}'.format(i + 1)
    # go into week folder
    os.chdir(week)
    os.makedirs("READ")
    os.makedirs("ASSIGNMENTS")
    os.makedirs("LAB")
    os.makedirs("DISCUSSIONS")
    # go into the discussions folder
    os.chdir("{}/{}/DISCUSSIONS".format(course_root_folder,week))
    dissDoc = "discussion_{}.docx".format(i + 1)
    # create a word file in the discussion folder
    open(dissDoc, "w")
    # go back up to the course folder
    os.chdir(course_root_folder)
print("Operation Complete")        
# oK this works as expected