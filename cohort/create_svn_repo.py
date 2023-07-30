import os
import shutil
import subprocess

# Set the specified permissions for the new directory
def set_permissions(directory_path):

    os.system(f'sudo chmod -R 775 $(find {directory_path} -type d)')
    os.system(f"sudo find {directory_path} -type f -exec chmod 666 {{}} +")


def change_ownership(directory_path, user, group):

    os.system(f"sudo chown -R {user}:{group}  {directory_path}")

# create new dir
def config_directory(repo_details):

    is_created = False

    # Parent Directory path
    parent_dir = "/home/SVN_REPOS/"
    # new repo path
    path = os.path.join(parent_dir, repo_details['repo'])

    try:
        if os.path.exists(path):

            # Delete dir
            os.system("sudo rm -rf " + parent_dir + repo_details['repo'])
            # Then make a new dir
            os.system("sudo mkdir " + parent_dir + repo_details['repo'])
            # change owner and group
            change_ownership(path, repo_details['user'], repo_details['group'])
            # set permission to the new directory
            set_permissions(path) 
            is_created = True
            # log event
            print(f"Previous directory:  {path} existed and was deleted")

        else:

            # make a new dir 
            os.system("sudo mkdir " + parent_dir + repo_details['repo'])
            # change owner and group
            change_ownership(path, repo_details['user'], repo_details['group'])
            # set permission to the new directory
            set_permissions(path)
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
    # get user name
    user_name = input("Enter User Name: ")
    # what type of repo are we making?
    repo_type = input("Enter Repo Type: (Git or SVN) ")

    print()
    print(f'You entered')
    print(f'Repository Type: {repo_type}')
    print(f'Repository Name: {repo_name}')
    print(f'Group Name: {group_name}')
    print(f'User Name: {user_name}')
    print()

    return {"repo": repo_name.lower().strip(), "group": group_name.strip(), "user": user_name.strip(), "type": repo_type.lower().strip()}


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

            
            if config_directory(repo_details):
                print(f"Success\nNew Directory: /home/SVN_REPOS/{repo_details['repo']}")
                # from this point determine git or svn
                if repo_details['type'] == "svn":
                    print(f"we need to make a {repo_details['type']} repository")

                elif repo_details['type'] == "git":
                    print(f"we need to make a {repo_details['type']} repository")

                else:
                    print(f"ERROR - Unsupported repo type: {repo_details['type']}")

            break


    





    
