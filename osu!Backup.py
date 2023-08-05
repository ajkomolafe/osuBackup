#osu!Backup, folder as osuBackup
import os
import shutil
import sys

songsDirectory = os.path.join(os.getenv('LOCALAPPDATA'), "osu!/Songs")
backupDirectory = os.path.join(os.getenv('LOCALAPPDATA'), "osu!/osuBackup")

#initialize
try:
    os.mkdir(backupDirectory)
except:
    print("osu!Backup directory already exists! To clear it for a new backup, enter 'Y'. Otherwise, script will stop.",end="\n")
    if input() == "Y":
        for i in os.scandir(backupDirectory):
            try: 
                #if folder
                shutil.rmtree(i.path)
            except: 
                #if single file
                os.remove(i.path)
    else:
        print("Script stopped.")
        sys.exit()

name = ""
nameList = []
while name != "Stop" and name != "stop":
    name = input("Enter all your host and guest usernames to backup \n")
    if name != "Stop" and name != "stop":
        nameList += ["("+name+")"]
        nameList += [name+"'s"]
print(nameList)
    
for beatmapset in os.scandir(songsDirectory): #for each beatmapset
    if beatmapset.is_dir():
        mapperExists = False
        for file in os.scandir(beatmapset):
            for mapperName in nameList:
                if mapperName in file.name and file.is_file():
                    mapperExists = True
    else:
        continue
    if mapperExists:
        print("Found Beatmap Folder: "+beatmapset.name)
        shutil.copytree(beatmapset.path, os.path.join(backupDirectory, beatmapset.name))
        
print("Your backup is complete!")