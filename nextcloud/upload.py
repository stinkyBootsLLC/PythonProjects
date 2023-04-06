# using this library https://pypi.org/project/pyncclient/
# https://pynative.com/python-list-files-in-a-directory/ 
# https://unc-libraries-data.github.io/Python/Files_Packages/Files_Packages.html
import nextcloud_client
import os
import config
import logging
import sys

def login_remote_location(username, password, nextcloud_client, logger):

    try:
        nextcloud_client.login(username, password)
    except:
        logger.error("could not login for " + username)
        sys.exit("could not login for " + username)



   
def main():
    """
    Main entry to application
    """

    logging.basicConfig(filename='script.log', filemode='a',
    format='%(asctime)s - %(msecs)d - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d - %H:%M:%S',level=logging.INFO)
    # Create an object 
    logger = logging.getLogger() 
    # Set the threshold of logger to DEBUG 
    logger.setLevel(logging.DEBUG) 
    # create the client object 
    nc = nextcloud_client.Client(config.next_cloud_location)

    login_remote_location(config.username, config.password, nc, logger)
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

if __name__ == "__main__": 
	print("Autoloader") 
	main() 