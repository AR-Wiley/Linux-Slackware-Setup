import os

rootDir = "/var/log/Sys_Admin"
subDir = ["Updates", "Software", "Downloads", "Users", "Scripts", "Admin"]

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

rootDirValidation(rootDir)
subDirValidation(rootDir,subDir)