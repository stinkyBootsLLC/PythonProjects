import nextcloud_client, os, config, logging, sys

from datetime import datetime

def upload_files(nextcloud_client):
    """ Uploads files to nextcloud instance

    Parameters
    ----------
    nextcloud_client : (nextcloud_client) The nextcloud client object
    """

    print("Uploading files ..............")

    try:
        # Get the list of all files and directories
        files_to_upload = os.listdir(config.local_path)
        
        for file in files_to_upload:

            if file != ".DS_Store":

                nextcloud_client.put_file(config.remote_path + file, config.local_path + file)
                logging.info('Uploaded - ' + file) 
                print('Uploaded - ' + file)

        logging.info("upload complete") 
        
    except:
        # log error and exit
        logging.error("files NOT uploaded")
        sys.exit("\033[31mERROR: files NOT uploaded\033[0m")
    

def login_remote_location(username, password, nextcloud_client):
    """ Logs into nextcloud instance
    
        Parameters
        ----------
        username : (str) The user's username
        password : (str) The user's password
        nextcloud_client : (nextcloud_client) The nextcloud client object
    """

    print("Login into nextcloud ..............")
    
    try:
        # log into account
        nextcloud_client.login(username, password)
        logging.info('login complete')

    except:
        # log error and exit
        logging.error("could not login for " + username)
        sys.exit("\033[31mERROR: could not login for \033[0m" + username)

    # upload files
    upload_files(nextcloud_client)

    print('\033[32mupload complete ........... {}\033[0m'.format(datetime.now()))

   
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
  
    logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', filename='upload.log',level=logging.DEBUG)

    main()
