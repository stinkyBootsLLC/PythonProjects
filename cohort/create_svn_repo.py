import os
import shutil
import subprocess

# Set the specified permissions for the directory
def set_permissions(directory_path):
   
    dir_command = 'sudo chmod -R 775 $(find ' + directory_path + ' -type d)'
    file_command = 'sudo chmod -R 666 $(find ' + directory_path + ' -type f)'

    os.system(dir_command)
    os.system(file_command)


# create new dir
def create_directory(repo_details):

    is_created = False

    # gid = grp.getgrnam(repo_details['group']).gr_gid
    user = 'centospypy'
    group = repo_details['group']

    # Parent Directory path
    parent_dir = "/home/SVN_REPOS/"
    # Path
    path = os.path.join(parent_dir, repo_details['repo'])
    try:
        if os.path.exists(path):
            # # Delete Folder code
            # os.rmdir(path) will not delete if there are items inside of it
            # shutil.rmtree(path)
            os.system("sudo rm -rf " + parent_dir + repo_details['repo'])
            # os.mkdir(path)
            os.system("sudo mkdir " + parent_dir + repo_details['repo'])

            set_permissions(path) 
            # shutil.chown(path, user, group)

            os.system("sudo chown -R "  + user + ":" + group + " " + parent_dir + repo_details['repo'] )
            
            is_created = True
  
            print("The folder has been deleted successfully!")
        else:
            # os.mkdir(path) 
            os.system("sudo mkdir " + parent_dir + repo_details['repo'])
            set_permissions(path)
            # shutil.chown(path, user, group)
            sudo chgrp -R geeksforgeeks GFG

            os.system("sudo chown -R "  + user + ":" + group + " " + parent_dir + repo_details['repo'] )




            is_created = True

    except OSError as error: 
        print(error)

    return is_created

# Get user input
def get_user_input():
    # get repo name
    repo_name = input("Enter Repository Name: ")
    # get group name 
    group_name = input("Enter Group Name: ")
    print()
    print(f'You entered')
    print(f'Repository Name: {repo_name}')
    print(f'Group Name: {group_name}')
    print()

    return {"repo": repo_name.lower(), "group": group_name}


if __name__ == "__main__": 
    print()
    print("............................................................")
    print("............................................................")
    print("..............SVN Repository Creator (v.1.0.0)..............") 
    print("............................................................")
    print("............................................................")
    print()

    while True:
        repo_details = get_user_input()
        correct = input("Is this information correct? (Y or N) ")
        if correct.lower() == 'y':
            
            if create_directory(repo_details):
                print('created')

            break


    





    
