import os
import shutil
import subprocess

"""Initializes a bare Git repository. 

 Args: 
    repo_name: string
    
 Returns: NONE

"""
def create_git_repo(repo_name):

    try:
        subprocess.run(["git", "init", "--bare", repo_name], cwd=repo_name, check=True)
        print(f"Git bare repository '{repo_name}' created successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
    except Exception as ex:
        print(f"An unexpected error occurred: {ex}")


"""Sets the specified permissions for the new directory. 

 Args: 
    directory_path: string
    
 Returns: NONE

"""
def set_permissions(directory_path):

    os.system(f'sudo chmod -R 775 $(find {directory_path} -type d)')
    os.system(f"sudo find {directory_path} -type f -exec chmod 666 {{}} +")

"""Sets the specified ownership for the new directory. 

 Args: 
    directory_path: string 
    user: string 
    group: string
    
 Returns: NONE

"""
def change_ownership(directory_path, user, group):

    os.system(f"sudo chown -R {user}:{group}  {directory_path}")

"""Configures a new directory. 

 Args: 
    repo_details: dictionary
    path: string

 Returns:
    is_created: Boolean

"""
def config_directory(repo_details, path):

    is_created = False

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


"""Gets the user input.

 Args: NONE
 Returns: NONE

"""
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

            # Parent Directory path
            parent_dir = "/data/data/version_control/"
            # new repo path
            complete_path = os.path.join(parent_dir, repo_details['repo'])

            if config_directory(repo_details, complete_path):

                print(f"New Directory: {complete_path} created successfully.")
                # from this point determine git or svn
                if repo_details['type'] == "svn":

                    print(f"we need to make a {repo_details['type']} repository")

                elif repo_details['type'] == "git":

                    print(f"we need to make a {repo_details['type']} repository")
                    create_git_repo(complete_path)

                else:

                    print(f"ERROR - Unsupported repo type: {repo_details['type']}")

            break


    





    
