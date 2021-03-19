# STIG Checklist Value Extractor

> Purpose: To extract certain attribute values from 
the [STIG VIEWER](https://public.cyber.mil/stigs/srg-stig-tools/) .ckl file for creating reports.
I wanted to extract specific values from the STIG Viewer application checklist (.ckl) file, 
to use for creating reports. 
 
Final Output Format

| V-id     | Severity |         Title          | Status      |     Detail      |      Comment         |
| ---------| ---------| -----------------------| ------------| ----------------|  --------------------|
| V-123456 | low      | Title of vulnerability | NotAFinding |settings not set | working on a solution!


 
## Getting Started

These instructions will get you a copy of the project up and running on your local machine 
for development and testing purposes.  

- Download this repository to your local machine. The XML (.ckl) file must be in the same directory
as the (.py) file. 
- Run the .py file from local directory and follow instructions 
on the console. **Note:** Use (example.ckl) as a test input file.
- The extension of the file DOES NOT MATTER as long as the file is a properly XML formatted file.
- The output file name can be anything you want - I like .csv to keep it simple
- ".ckl" must follow the same tree structure as "example.ckl" in this repository
- Once the program is complete, use Excel (or any other spreadsheet program) to IMPORT the newly created file. 
(The one you named).

### Prerequisites

Must have Python 3.8 installed on host machine. Get [Python](https://www.python.org/downloads) 

## Version

1.0

## Author

Eduardo Estrada | Created Date: 3/11/2021

## License

This project is licensed under the MIT License - see the [LICENSE.md](https://www.mit.edu/~amini/LICENSE.md) file for details

## Acknowledgments

*  NONE


