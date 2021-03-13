# STIG Checklist Value Extractor
> Purpose: To extract certain attribute values from the [STIG VIEWER](https://public.cyber.mil/stigs/srg-stig-tools/) .ckl file for reports 


| Name | Value |
| ------ | ------ |
| File Name: |   |
| Created Date: | 3/11/2021 |
| Author: | Eduardo Estrada|


# Methods
- get_ckList_info
- make_csv_file

#### get_ckList_info(file_name):

| Parameter | Type | Description |
| ------ | ------ |------ |
| file_name: |  String | input xml file name
    
| Returns | Type | Description |
| ------ | ------ |------ |
| final_list: |  List | list of attribute values from the xml file


> Returns a list of the following attributes from the specific stig-viewer xml file.

- V-id
- Severity
- Title
- Status
- Detail
- Comment
	
	
**Note:** V-id, Severity and Title are combined to one string


#### make_csv_file(fileName,list):

| Parameter | Type | Description |
| ------ | ------ |------ |
| fileName: |  String | Output file name
| list: |  List | the list to make the output file from

| Returns | Type | Description |
| ------ | ------ |------ |
| ...  | Void | Creates the file in the current directory

> Creates a delimited file in this current directory based on the parameter list. In this script the delimiter is the pipe (|) character.

## How it works
I wanted to extract specific values from the STIG Viewer application checklist file, to use for creating reports.
Run the .py file from local directory and follow instructions on the console.
- the extension of the file DOES NOT MATTER as long as the file a properly XML formatted file.
- The input file will have the .ckl extension.
- The output file name can be anything you want - I like .txt to keep it simple

**Note:**".ckl" must follow the same tree structure as "example.ckl" in this repository

Once the program is complete, use Excel to IMPORT the newly created file. (The one you named)
- Use the (|) character as the delimiter.

| V-id     | Severity | Title                  | Status      | Detail          | Comment             |
| -----    | ---------| -----------------------| ------------| ----------------|  -------------------|
| V-123456 | low      | Title of vulnerability | NotAFinding |settings not set | working of solution!








## License
MIT
**Free Software, Hell Yeah!**
