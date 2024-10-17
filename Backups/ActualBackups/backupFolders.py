#!/bin/python3

import os
from subprocess import Popen, PIPE

# get current py file path
pwd = os.path.dirname(os.path.realpath(__file__))
print(pwd)


# probably won't work well with files since / is not with folders
class backupNewVolume:
    def __init__(self, backupDest1):
        self.dest = backupDest1
        self.backupList = []
        self.file_path = pwd
        
        if not os.path.exists(f"{self.file_path}/addBackups.txt"):
            with open(f"{self.file_path}/addBackups.txt",'w') as f:
                f.write("")
        with open(f"{self.file_path}/addBackups.txt",'r') as f:
            for line in f:
                self.backupList.append(line.strip())
    
    def backupFolders(self):
        print(self.backupList)
        for src in self.backupList:
            
            # use rclone to copy files with backup-dir
            if src[-1] != "/":
                folder = str(src).split('/')[-1]
            else:
                folder = str(src).split('/')[-2]
            cmd = ["rclone", "sync", src, self.dest+"/"+folder, "--progress"]
            print(cmd)
            p = Popen(cmd, stdout=PIPE, stderr=PIPE)
            stdout, stderr = p.communicate()
            print(stdout.decode())
            if len(stderr) > 0:
                print(stderr.decode())
            print("-"*90) 
            # print("-"*90)
            
            
            
            
        print("TEST", self.backupList)
        
    def verify(self, path):
        # check path exists
        
        if not os.path.exists(path):
            print(f"Path does not exist: \'{path}\'")
            return False
        return True
        
    def addBackup(self, src):
        if self.verify(src):
            self.backupList.append(src)
        else:
            print("Path does not exist")
            
    def loadtxt(self, path):
        with open(path, "r") as f:
            for line in f:
                self.addBackup(line.strip())

    def save(self, path):
        # check for duplicates
        self.backupList = list(set(self.backupList))
        with open(path, "w") as f:
            for line in self.backupList:
                f.write(line + "\n")
                
    def default(self):
        file_path = pwd + "/files.txt"
        self.loadtxt(file_path)
        self.save(file_path)
    
    


# for src, dest in backup_list.items():
#     backupFolders(src, dest)
backupDest1 = r"/media/lunachocken/New Volume/Backups/"

backup = backupNewVolume(backupDest1)
backup.default() # load files.txt


backup.addBackup("/home/lunachocken/Documents/Tools")
backup.addBackup(r"/home/lunachocken/.steam/steam/steamapps/compatdata/3872367365/pfx/drive_c/users/steamuser/AppData/Roaming/EldenRing")
backup.addBackup(r"/home/lunachocken/.var/app/org.prismlauncher.PrismLauncher/data/PrismLauncher/instances/")

backup.backupFolders()