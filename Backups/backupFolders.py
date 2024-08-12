import os, shutil

def backupFolders(src, dest):
    shutil.copytree(src, dest+"/")

backup_list = {
    "/home/lunachocken/Documents/Tools": "/media/lunachocken/New Volume/Backups/"
}


for src, dest in backup_list.items():
    backupFolders(src, dest)
    