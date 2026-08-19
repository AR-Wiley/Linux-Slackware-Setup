import os
import sys

rootDir = "/var/log/Sys_Admin"
subDir = ["Updates", "Software", "Downloads", "Users", "Scripts", "Admin"]

def check_root():

        if os.getuid() != 0:
                print("This sript must be run as root", file=sys.stderr)
                sys.exit(1)

def rootDirValidation(path):
        
        if not os.path.exists(path):
                print("Root path does not exist...")
                print("Creating path...")
                try:
                        os.makedirs(path)
                        print(f"{path} had been created")
                        print(path)
                except Exception as e:
                        print(f"An error has occured: {e}")
        else:
                print(path)


def subDirValidation(rootDir, subDir):
        
        for i in subDir:
                if not os.path.exists(os.path.join(rootDir, i)):
                        print("Sub directory path does not exist...")
                        print("Creating sub directory...")
                        try:
                                os.makedirs(os.path.join(rootDir, i))
                                print(f"Sub directory {i} created successfully")
                        except Exception as e:
                                print(f"An error hsa occurred: {e}")
                else:
                        print(f"Sub directory {i} already exists")


check_root()
rootDirValidation(rootDir)
subDirValidation(rootDir,subDir)
