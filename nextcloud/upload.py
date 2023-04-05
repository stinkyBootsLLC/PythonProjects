# using this library https://pypi.org/project/pyncclient/
import nextcloud_client
import os
import config
 
nc = nextcloud_client.Client(config.next_cloud_location)

# nc.login('eponch@yahoo.com', 'Gofuckyourself')

nc.login(config.username, config.password)

# nc.mkdir('AutoLoaded')
# Get the list of all files and directories
# https://pynative.com/python-list-files-in-a-directory/ 
# https://unc-libraries-data.github.io/Python/Files_Packages/Files_Packages.html
path = "/Users/eduardo/Desktop/AutoLoaded/"
files_to_upload = os.listdir(path)

for file in files_to_upload:

    nc.put_file('AutoLoaded/' + file, '/Users/eduardo/Desktop/AutoLoaded/' + file)

    print('Uploaded - AutoLoaded/' + file)

    # link_info = nc.share_file_with_link('AutoLoaded/' + file)

    # print("Here is your link: " + link_info.get_link())

print('complete')