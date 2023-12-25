""" 
Name: create_git_repo.py
Description: Creates GIT repository with standard configuration
Author: Eduardo Estrada
Date: 12/5/2023
"""
import datetime, argparse, os, subprocess

from pathlib import Path
 
def create_directory(directory):
    """Creates a new directory was created

    Args:
    directory (pathlib.PosixPath): Absolute directory path 

    Returns: is_created (boolean): Returns True if new directory was created
    """
    is_created = False

    if os.path.exists(directory):
        # throw execption
        raise Exception(f"Repo: '{directory}' Already Exists!")

    else:
        # make directory
        directory.mkdir()

        is_created = True
    
    return is_created

def add_file(file_path, content):
    """Adds a new file to a directory

    Args:
    file_path (pathlib.PosixPath): full path to new file
    content (str): content to be added to file 

    Returns: is_added (boolean): Returns True if new file was created
    """

    is_added = False
    
    try:
        new_file = open(file_path, mode="w") 
        new_file.write(content)
        is_added = True
    except Exception as ex:
        print(ex)
        raise Exception(ex)
            
    return is_added



def display_message(new_repo_name):
    """ Displays message """
     
    print(f""" 
        ............................................................
        ............................................................
        ...................... Version Control .....................
        ..................... Repository Creator ...................
        ........................ 2023 v.1.0.0 ......................
        ............................................................
        ............................................................

        NEW PROJECT CREATED: {new_repo_name}


    """)

def main(new_repo_name, alt_repo_name=None):
    """Main script entry.

    Args:
    new_repo_name (parsed argument): New repository name
    alt_repo_name (optional parsed argument): New repository name (alternate location)

    """
    if alt_repo_name:
        new_git_path = Path(alt_repo_name)
    else:
        new_git_path = Path.cwd().absolute() / new_repo_name

    if create_directory(new_git_path):

        added_file = add_file((new_git_path / "README.md"), (f"# {new_repo_name}"))

        added_file = add_file((new_git_path / ".gitignore"), "\n".join(["__pycache__", "*.txt", "**/.DS_Store"]))

        # init the new dir as a git repo
        if added_file:

            commands = [
                ["git", "-C", new_repo_name, "init"],
                ["git", "-C", new_repo_name, "add", "--all"],
                ["git", "-C", new_repo_name, "commit", "-m", "init commit"],
            ]

            # run all the commands
            for command in commands:
                subprocess.run(command, check=True, timeout=60)

            display_message(new_git_path)

        else:
            print("Files not added")

    else:
        print("Something went wrong")

            
if __name__ == "__main__":

    # passing in arguments in command line
    parser = argparse.ArgumentParser()
    
    parser.add_argument("--repository_name", "-rN", type=str)
    """Reguired Argument [ --repository_name, -rN ] The new directory to create the GIT repo (Current Directory)"""

    parser.add_argument("--alt_repository_name", "-aRN", type=str)
    """Optional Argument [ --alt_repository_name, -aRN ] Provide an alternate directory """

    args = parser.parse_args()

    try:
        if args.repository_name:

            main(args.repository_name)

        elif args.alt_repository_name:

            main(args.alt_repository_name)

        else:

            raise Exception("Repository Name was not provided?")

    except Exception as ex:

        print(f"Execption: {ex}")
