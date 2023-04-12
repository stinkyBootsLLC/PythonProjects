import nextcloud_client
import os
import config
import logging
import sys


def upload_files(nextcloud_client, logger):
    """ Uploads files to nextcloud instance

    Parameters
    ----------
    nextcloud_client : nextcloud_client
        The nextcloud client object
    logger : logging
        The logging object
    """

    print("Uploading files ..............")

    try:
        # Get the list of all files and directories
        files_to_upload = os.listdir(config.local_path)
        
        for file in files_to_upload:

            if file != ".DS_Store":

                nextcloud_client.put_file(config.remote_path + file, config.local_path + file)
                logger.info('Uploaded - ' + file) 
                print('Uploaded - ' + file)
                # link_info = nc.share_file_with_link('AutoLoaded/' + file)
                # print("Here is your link: " + link_info.get_link())

        logger.info("upload complete") 
        
    except:
        # log error and exit
        logger.error("files NOT uploaded")
        sys.exit("ERROR: files NOT uploaded")
    

def login_remote_location(username, password, nextcloud_client, logger):
    """ Logs into nextcloud instance
    
    Parameters
    ----------
    username : str
        The user's username
    password : str
        The user's password
    nextcloud_client : nextcloud_client
        The nextcloud client object
    logger : logging
        The logging object
    """

    print("Login into nextcloud ..............")
    
    try:
        # log into account
        nextcloud_client.login(username, password)
        print('login complete')

    except:
        # log error and exit
        logger.error("could not login for " + username)
        sys.exit("ERROR: could not login for " + username)

    # upload files
    upload_files(nextcloud_client, logger)
    print('upload complete')

   
def main():
    """ Main entry to application

    """

    # set logger configuration
    logging.basicConfig(filename='script.log', filemode='a',
    format='%(asctime)s - %(msecs)d - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d - %H:%M:%S',level=logging.INFO)
    # Create an object 
    logger = logging.getLogger() 
    # Set the threshold of logger to DEBUG 
    logger.setLevel(logging.DEBUG) 
    # create the nextcloud client object 
    nc = nextcloud_client.Client(config.next_cloud_location)
    # call function
    login_remote_location(config.username, config.password, nc, logger)
    # nc.mkdir('AutoLoaded')

if __name__ == "__main__": 
	print("Autoloader started (v.1.0.1)..............") 
	main() 