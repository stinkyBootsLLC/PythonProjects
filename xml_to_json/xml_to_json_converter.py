"""
File Name:
Created Date: 3/11/2021
Author: Eduardo Estrada
Purpose: To extract certain attribute values from the STIG VIEWER .ckl file for reports
"""
# Importing the required libraries 
import logging
import json
import xml.etree.ElementTree as Xet 
import re
 
 
def get_ckList_info(file_name):
	"""
	Returns a list of the following attributes from the specific stig-viewer
	xml file.

	"vulnID | Severity | Title | Status | Detail | Comment"   

	Parameters
    ----------
    file_name : string
       	name of the xml file
    Returns
    -------
    final_list: List
        list of attribute values from the xml file
	"""

	logging.info('get_ckList_info() Started')
	# method local variables
	# 
	stig_vulNum_results = []
	stig_title_results = []
	stig_sevirity_results = []
	stig_status_results = []
	stig_findingDetails_results = []
	stig_comments_results = []
	# temp_dict = {}
	final_list = []

	try:
		tree = Xet.parse(file_name)
		stigData = tree.findall('STIGS/iSTIG/VULN/STIG_DATA')
		stigStatus = tree.findall('STIGS/iSTIG/VULN')
		stigFindingDetails = tree.findall('STIGS/iSTIG/VULN')
		stigComments = tree.findall('STIGS/iSTIG/VULN')
		#  
		header = '{ "vulnerabilities": ['
		footer = ']}'
		final_list.append(header)
		# get all stig data 
		for data in stigData:
			Vuln_Attr = data.find('VULN_ATTRIBUTE').text
			if Vuln_Attr == 'Vuln_Num':
				# then get the attribute
				vuln_id = data.find('ATTRIBUTE_DATA').text
				stig_vulNum_results.append(vuln_id)
			if Vuln_Attr == 'Severity':
				# then get the attribute
				vuln_seve = data.find('ATTRIBUTE_DATA').text
				stig_sevirity_results.append(vuln_seve)
			if Vuln_Attr == 'Rule_Title':
				# then get the attribute
				vuln_title = data.find('ATTRIBUTE_DATA').text
				cleanTitle = re.sub(r'[^\w]', ' ', str(vuln_title))
				stig_title_results.append(cleanTitle)
		# get all status
		for data in stigStatus:
			Vuln_Stat = data.find('STATUS').text
			stig_status_results.append(Vuln_Stat)
		# get all finding details
		for data in stigFindingDetails:
			find_details = data.find('FINDING_DETAILS').text
			cleanDetail = re.sub(r'[^\w]', ' ', str(find_details))
			stig_findingDetails_results.append(cleanDetail)
		# get all comments
		for data in stigComments:
			find_details = data.find('COMMENTS').text
			stig_comments_results.append(find_details)
		# # create a dictionary /hashmap /not being used yet
		# # for future use try to create JSON format
		# temp_dict["ID_Title"] =  stig_data_results
		# temp_dict["Status"] =  stig_status_results
		# temp_dict["Details"] =  stig_findingDetails_results
		# temp_dict["Comments"] =  stig_comments_results
		# combine the four list into the final list
		for i in range(len(stig_findingDetails_results)):
			id = stig_vulNum_results[i]
			title = stig_title_results[i]
			sevirity = stig_sevirity_results[i]
			status = stig_status_results[i]
			detail = stig_findingDetails_results[i]
			comment = stig_comments_results[i]
			row = '{{ "vulnID": "{}", "Title": "{}", "severity": "{}","Status": "{}","Detail": "{}","Comment": "{}" }},'.format(
				id, title, sevirity, status,detail,comment )
			final_list.append(row)

		final_list.append(footer)
	except Exception as e:
		print("There was an error please check log file")
		logging.error(e)
	finally:
	 
		logging.info('Stig status vulNum size: {}'.format(len(stig_vulNum_results)))
		logging.info('Stig Title results size: {}'.format(len(stig_title_results)))
		logging.info('Stig sevirity results size: {}'.format(len(stig_sevirity_results)))
		logging.info('Stig status results size: {}'.format(len(stig_status_results)))
		logging.info('Stig finding details results size: {}'.format(len(stig_findingDetails_results)))
		logging.info('Stig comments results size: {}'.format(len(stig_comments_results)))

		return final_list

def make_csv_file(fileName,list):
	"""
	Creates a file
		Parameters
    ----------
    fileName : string
       	name of the output file
	list : List
		the list to make the output file from	   
    Returns
    -------
    Void
        Makes the file in the current directory
	"""
	logging.info('Making CSV Started')	
	# write once
	with open(fileName, 'w') as filehandle:
		for item in list:
			filehandle.write('%s\n' % item)
	print("Script has finished running - thanks for playing and see you soon!") 

def main():
	"""
	Main entry to application
	"""

	logging.basicConfig(filename='App.log', filemode='a',
		format='%(asctime)s - %(msecs)d - %(name)s - %(levelname)s - %(message)s',
		datefmt='%Y-%m-%d - %H:%M:%S',level=logging.INFO)

	logging.info('Application Started')	
    # prompt user for input
	inputFileName = input("Enter the input file name:  ").lower()
	outputFileName = input("Enter the OUTPUT file name:  ").lower()
	logging.info('InputFile: {} OutputFile: {}'.format(inputFileName,outputFileName))	
	# parse the xml file
	checkList = get_ckList_info(inputFileName)
	# create a deliminated file.
	make_csv_file(outputFileName,checkList)
	logging.info('Application is finished')
	

if __name__ == "__main__": 
	print("Welcome to the my xml parser") 
	print("File inputs must be in XML format\n") 
	main() 
