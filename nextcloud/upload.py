# using this library https://pypi.org/project/pyncclient/
# https://pynative.com/python-list-files-in-a-directory/ 
# https://unc-libraries-data.github.io/Python/Files_Packages/Files_Packages.html
import nextcloud_client
import os
import config
import logging


logging.basicConfig(filename="script.log", format='%(asctime)s %(message)s', filemode='a') 
# Create an object 
logger=logging.getLogger() 
# Set the threshold of logger to DEBUG 
logger.setLevel(logging.DEBUG) 
 
nc = nextcloud_client.Client(config.next_cloud_location)
nc.login(config.username, config.password)
# nc.mkdir('AutoLoaded')
# Get the list of all files and directories
files_to_upload = os.listdir(config.local_path)

for file in files_to_upload:

    nc.put_file(config.remote_path + file, config.local_path + file)
    logger.info('Uploaded - ' + file) 
    print('Uploaded - ' + file)
    # link_info = nc.share_file_with_link('AutoLoaded/' + file)
    # print("Here is your link: " + link_info.get_link())

logger.info("complete") 
print('complete')