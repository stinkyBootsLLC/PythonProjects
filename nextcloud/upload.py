"""_summary_ """
import os
import sys
import logging
from datetime import datetime
import nextcloud_client
import config

def get_logger():
    """_summary_

    Returns:
        logger: logger
    """
    log_file_location = config.log_file 
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    # create file handler which logs even debug messages
    fh = logging.FileHandler(log_file_location)
    fh.setLevel(logging.DEBUG)
    # create console handler with a higher log level
    ch = logging.StreamHandler()
    ch.setLevel(logging.ERROR)
    # create formatter and add it to the handlers
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)
    # add the handlers to the logger
    logger.addHandler(fh)
    logger.addHandler(ch)
    return logger



def upload_files(next_cl):
    """ Uploads files to nextcloud instance

    Parameters
    ----------
    nextcloud_client : (nextcloud_client) The nextcloud client object
    """
    logger = get_logger()
    
    print("Uploading files ..............")
    logger.info('Uploading files ...')

    try:
        # Get the list of all files and directories
        files_to_upload = os.listdir(config.local_path)
        
        for file in files_to_upload:

            if file != ".DS_Store":

                next_cl.put_file(config.remote_path + file, config.local_path + file)
              
                print('Uploaded - ' + file)
                logger.info('Uploaded - %s', file)

        logger.info("upload complete ........... ")
        print(f'\033[32mupload complete ........... {datetime.now()}\033[0m')
        
    except Exception as ex:
        # log error and exit
        logger.error('ERROR: files NOT uploaded %s', ex)
        sys.exit("\033[31mERROR: files NOT uploaded\033[0m")
    

def login_remote_location(username, password, next_cl):
    """ Logs into nextcloud instance
    
        Parameters
        ----------
        username : (str) The user's username
        password : (str) The user's password
        nextcloud_client : (nextcloud_client) The nextcloud client object
    """
    logger = get_logger()
    print("Login into nextcloud ..............")
    logger.info("Login into nextcloud ..............")
    
    try:
        # log into account
        next_cl.login(username, password)
        # upload files
        upload_files(next_cl)
      
    except Exception as ex:
        print()
        logger.error("ERROR: %s", ex)
        logger.error("ERROR: could not login for %s", username)
        sys.exit("\033[31mERROR: could not login for \033[0m" + username)
        



    


def main():
    """ Main entry to application """

    print("""
    .........................................
    ...... \033[34mAutoloader started (v.1.0.4)\033[0m .....
    .........................................
    """)

    nc = nextcloud_client.Client(config.next_cloud_location)
    # call function
    login_remote_location(config.username, config.password, nc)

if __name__ == "__main__":

    main()
