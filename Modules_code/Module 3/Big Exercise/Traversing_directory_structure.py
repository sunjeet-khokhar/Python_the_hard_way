import os 
import re

dir_to_search = "D:\Code"
os.chdir(dir_to_search)

print('Double check your folders for deletion here---->\n')
for root,dirs,files in os.walk(dir_to_search, topdown=True):
    
    for dir in dirs:
        match = re.search(r'For_deletion*',dir)
        if (match is None):
            continue
        else:
            #print absolute path of the directory
            print(os.path.join(root,dir))

print('\nDouble check your files for deletion here--->\n')
for root,dirs,files in os.walk(dir_to_search, topdown=True):
    
    for file in files:
        match = re.search(r'For_deletion',file)
        if (match is None):
            continue
        else:
            print(os.path.join(root,file))
            
# TBD - code to delete files and folders
        