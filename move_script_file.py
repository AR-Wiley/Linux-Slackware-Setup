import os
import shutil
import sys

source_path = "/home"
destination_path = "/home/Scripts"

def validate_home_path(path):

        if not os.path.exists(path):
                print("Path does not exist. Validation failed")
                sys.exit(1)

def validate_destination_path(path):

        if not os.path.exists(path):
                print("Path does not exist.")
                print("Creating path")
                try:
                        os.makedirs(path)
                        print(f"{path} has been create")
                        print(path)
                except Exception as e:
                        print(f"An error has occured: {e}")

def move_file(source_path, destination_path):

        if path.endswith((".py", ".sh")):
                try:
                        shutil.move(source_path, destination_path)
                        print(f"File moved to {destination_path}")
                except Exception as e:
                        print(f"An error has occured: {e}")
        else:
                print(f"No files to move to {destination_path}")


validate_home_path(source_path)
validate_destination_path(destination_path)
move_file(source_path, destination_path)
