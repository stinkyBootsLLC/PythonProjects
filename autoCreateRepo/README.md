# Auto Create GIT Repository

## Purpose

Creates a local Git source control repository.

## Getting Started

Application arguments

`--repository_name, -rN`: New repository name

`--alt_repository_name, -aRN`: New repository name (alternate location). **Provide full path**

### Installation

Download file `https://github.com/stinkyBootsLLC/PythonProjects/blob/main/autoCreateRepo/create_git_repo.py`

### Dependencies

- Python 3.8
    - datetime module 
    - argparse module
    - os module
    - subprocess module
    - pathlib module

_these modules come standard with the pyhon package_

### Usage

To Create a new repository in the current directory

```
python create_vc_repo.py --repository_name <new_repo_name>
# or
python create_vc_repo.py -rN <new_repo_name> 
```

To Create a new repository in an alternate directory 

```
python create_vc_repo.py --alt_repository_name <path/to/new/repo>
# or
python create_vc_repo.py -aRN <path/to/new/project> 
```

## Version History

- 1.0.0
    - Initial Release

## License

This project is licensed under the [The Unlicense](https://choosealicense.com/licenses/unlicense/).