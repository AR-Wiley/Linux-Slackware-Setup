#!/usr/bin/python3

import os
import sys

rootDir = "/var/log/Sys_Admin"
logFiles = ["updates.log", "installs.log", 
            "removals.log", "users.log", 
            "scripts.log", "security.log", "network.log"]

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
            print(f"{path} has been created")
            print(path)
        except Exception as e:
            print(f"An error has occured: {e}")
    else:
        print(path)

def logFileValidation(path, files):
        
    for i in files:
        file_path = os.path.join(path, i)
        if not os.path.isfile(file_path):
            print(f"Log file {i} does not exist")
            print(f"Creating file {i}")
            try:
                with open(file_path, "x") as f:
                    f.write(f"{i} ceated")
                    print(f"Created: {i}")
            except Exception as e:
                print(f"An error has occured: {e}")
        else: 
            print(f"File {i} already exists")


check_root()
rootDirValidation(rootDir)
logFileValidation(rootDir,logFiles)
