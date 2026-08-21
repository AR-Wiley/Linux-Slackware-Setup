
import os
import sys


home_dir = "/home"

root_dir =["Scripts", "Text", "Data", "Users", "Downloads", "Videos", "Pictures"]

def check_root():

        if os.getuid() != 0:
                print("This sript must be run as root", file=sys.stderr)
                sys.exit(1)

def homeDirValidation(path):

        if not os.path.exists(path):
                print(f"{home_dir} does not exist...")
                sys.exit(1)


def rootDirValidation(homeDir, rootDir):

        for i in rootDir:
                if not os.path.exists(os.path.join(homeDir, i)):
                        print(f"{i} does not exist...")
                        print(f"Creating {i}...")
                        try:
                                os.makedirs(os.path.join(homeDir, i))
                                print(f"{i} successfully created")
                        except Exception as e:
                                print(f"An error has occurred: {e}")
                else:
                        print(f"{i} already exists")

check_root()
homeDirValidation(home_dir)
rootDirValidation(home_dir, root_dir)

