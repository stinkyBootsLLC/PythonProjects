import os
import shutil

# create new dir
def create_repo(repo_details):
    is_created = False
    # Parent Directory path
    parent_dir = "/Users/eduardo/Desktop/SVNarea"
    # Path
    path = os.path.join(parent_dir, repo_details['repo'])
    try:
        if os.path.exists(path):
            os.rmdir(path)
      
            # # Delete Folder code
            # shutil.rmtree(folderPath)
            os.mkdir(path) 
            is_created = True
  
            print("The folder has been deleted successfully!")
        else:
            os.mkdir(path) 
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


 
        







# set new dir perm

# set new dir user and group

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
            
            if create_repo(repo_details):
                print('created')

            break


    





    
