

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


 
        





# create new dir

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
        repo_config = get_user_input()
        correct = input("Is this information correct? (Y or N) ")
        if correct.lower() == 'y':
            print('break loop and create repo')
            print(repo_config)
            break


    





    
