

# Get user input
def get_user_input():
    # get repo name
    repo_name = input("Enter Repository Name: ")
    # get group name 
    group_name = input("Enter Group Name: ")
    print(f'\nYou entered')
    print(f'Repository Name: {repo_name}')
    print(f'Group Name: {group_name}\n')


 
        





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
        get_user_input()
        correct = input("Is this information correct? (Y or N) ")
        if correct.lower() == 'y':
            print('break loop and create repo')
            break


    





    
