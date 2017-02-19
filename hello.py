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

print(fileMostRecent)

# Delete any file in the Downloads folder which hasn't been modified in over 2 weeks
now = time.time()
cutoff = now - (60*60*24*14) # 2 weeks ago
for file in os.listdir(path):
	attributes = os.stat(os.path.join(path, file))
	if attributes.st_mtime < cutoff:
		try:
			os.remove(os.path.join(path, file))
		except OSError:
			print(OSError.strerror)