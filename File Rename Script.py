#-----------------------------------------------------------
# File Rename Script by Terragon.de
#-----------------------------------------------------------

from os import rename, listdir

#-----------------------------------------------------------
# Make Configuration here:
#-----------------------------------------------------------


search = ".jpeg"		#Search this String
replace = ".jpg"		#Replace with this String
path = "Bilder/"		#Directory path relative to this python file


#-----------------------------------------------------------
# DO NOT CHANGE THIS!
#-----------------------------------------------------------

fnames = listdir(path)
for fname in fnames:
    fnamepath = path + fname
    rename(fnamepath, fnamepath.replace(search, replace, 1))