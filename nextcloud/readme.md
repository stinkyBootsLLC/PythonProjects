# My NextCloud Auto Uploader

Made this project for learning purposes. I needed an example to kick off some type of automation process. This script will upload every file from my personal computer to my self-hosted Nextcloud instance.

## Installation

1. Create your own python dev enviroment OR `git clone` this one.
2. You will need your own self-hosted Nextcloud instance.
3. Create `config.py` in the project root directory. 

```py
username = "<nextcloud username>"
password = "<nextcloud password>"
next_cloud_location = ""
local_path = "" # a directory on my laptop
remote_path = "" # a directory in nextcloud
log_file = "" # path/to/logfile.log
```
config.py

4. `python upload.py` runs the script
 
> :warning: Do not run from the same dir the files that need to be upload is located
 


## Support

NONE

## License

The project is licensed under the [Unlicense](https://unlicense.org/).

## References

- Python library to provide compatibility with nextCloud https://pypi.org/project/pyncclient/
- NextCloud Documentation https://docs.nextcloud.com/
- Python List Files in a Directory https://pynative.com/python-list-files-in-a-directory/
- Reading and Writing Files from Python https://unc-libraries-data.github.io/Python/Files_Packages/Files_Packages.html


