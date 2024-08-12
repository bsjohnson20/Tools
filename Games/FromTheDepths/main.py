import shutil

# Take workshop files and copy them
workshop_path = r"/home/lunachocken/.steam/debian-installation/steamapps/workshop/content/268650/"
destination_path = r"/home/lunachocken/From The Depths/Mods/"

def copyFiles(src, dest):
    shutil.copytree(src, dest,dirs_exist_ok=True)

# def renameFiles