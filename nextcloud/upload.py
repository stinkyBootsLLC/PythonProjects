# using this library https://pypi.org/project/pyncclient/
# https://pynative.com/python-list-files-in-a-directory/ 
# https://unc-libraries-data.github.io/Python/Files_Packages/Files_Packages.html
import nextcloud_client
import os
import config
 
nc = nextcloud_client.Client(config.next_cloud_location)
nc.login(config.username, config.password)
# nc.mkdir('AutoLoaded')
# Get the list of all files and directories
files_to_upload = os.listdir(config.local_path)

for file in files_to_upload:

    nc.put_file(config.remote_path + file, config.local_path + file)
    print('Uploaded - ' + file)
    # link_info = nc.share_file_with_link('AutoLoaded/' + file)
    # print("Here is your link: " + link_info.get_link())

print('complete')