import os, time

from datetime import datetime

# Find the most recent file in the Downloads folder
path = os.path.join('C:\\Users\\Martin\\Downloads')
tmp = 0
for file in os.listdir(path):
	attributes = os.stat(os.path.join(path, file))
	if attributes.st_mtime > tmp:
		tmp = attributes.st_mtime
		fileMostRecent = file
