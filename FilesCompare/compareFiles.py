"""
File: compareFiles.py
Created Date: 9/12/2021
Purpose: Compare two text files for different and common lines between the two files.

- Open both files in read mode
- Store list of strings
- Start comparing both files with the help of intersection() method for common strings
- Compare both files for differences using while loop
- Output results to external file
- Close both files

""" 
from datetime import datetime

def compare_two_files(file_1_name, file_2_name, output_file_name):
    """
    Compare the different and common lines between two files and output the results to output_file_name.
    In the output file the '@' character represents file 1 and the '#' represents file 2.

    Args:
      file_1_name: File 1 name (String)
      file_2_name: File 2 name (String)
      output_file_name: Output file name (String)

    Returns: void
    """
    # create a timestamp
    oDateTime = datetime.now()
    sTimestamp = oDateTime.strftime("%d-%b-%Y (%H:%M:%S)")
    # Open File in Read Mode
    file_1 = open(file_1_name, 'r')
    file_2 = open(file_2_name, 'r')
    # get each line from each file
    file_1_line = file_1.readline()
    file_2_line = file_2.readline()

    # Use as a Counter for the line number
    line_no = 1
    # open the input files
    print("starting routine")
    with open(file_1_name) as file1:
        with open(file_2_name) as file2:
            same = set(file1).intersection(file2)
    print("finished opening files")
    # write results to output file
    with open(output_file_name, 'w') as file_out:
        file_out.write(sTimestamp + "\n")
        file_out.write('Comparing files  (@' + file_1_name + 'and  (# '+ file_1_name + '\n')
        file_out.write("Common Lines in Both Files\n")
        for line in same:
            file_out.write(line)
        file_out.write("\nDifferent Lines in Both Files\n")
        # 
        while file_1_line != '' or file_2_line != '':
            # Removing whitespaces
            file_1_line = file_1_line.rstrip()
            file_2_line = file_2_line.rstrip()
            # Compare the lines from both file
            # if the lines DO NOT match
            if file_1_line != file_2_line:
                # otherwise output the line on file1 and use @ sign
                if file_1_line == '':
                    file_out.write("@ Line " + str(line_no) + " " + file_1_line + "\n")
                else:
                    file_out.write("@ Line " + str(line_no) + " " + file_1_line + "\n")
                    
                # otherwise output the line on file2 and use # sign
                if file_2_line == '':
                    file_out.write("# Line " + str(line_no) + " " + file_2_line + "\n")
                else:
                    file_out.write("# Line " + str(line_no) + " " + file_2_line + "\n")
            # Read the next line from the file
            file_1_line = file_1.readline()
            file_2_line = file_2.readline()
            # increment line number
            line_no += 1
    # close file streams
    file_1.close()
    file_2.close()
    file1.close()
    file2.close()
    file_out.close()
    print("routine complete")

def doFilesExist(fileOneName, fileTwoName):
    """
    Returns true if the two files exists.
    
    Args:
      fileOneName: File 1 name (String)
      fileTwoName: File 2 name (String)

    Returns: Boolean
    """
    foundFiles = False
    try:
        file_1 = open(fileOneName, 'r')
        file_2 = open(fileTwoName, 'r')
        foundFiles = True
    except OSError as ex:
        print("File: " + fileOneName + " or File: " + fileTwoName + " not found in this ROOT directory")
        print(ex)

    return foundFiles

def main():
    """
    Main entry to application
    """
    print("starting routine")
    print("Files MUST be in THIS root directory")
    fileOneName = input("Enter file 1 name ")
    fileTwoName = input("Enter file 2 name ")
    # check if the files exist
    if doFilesExist(fileOneName, fileTwoName):
        outFileName = input("Enter output file name ")
        compare_two_files(fileOneName, fileTwoName, outFileName)
    else:
        print("Error opening input files")
        print("routine was NOT completed")

if __name__ == "__main__": 
	print("Welcome to the my file comparison") 
	main()
