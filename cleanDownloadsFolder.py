import os
import glob

# list of file formats to delete
formats_to_delete = ['.exe', '.msi']

# navigate to downloads folder
os.chdir('C:/Users/<Username>/Downloads')

# find all files with the specified formats and delete them
for file in glob.glob('*'):
    if file.endswith(tuple(formats_to_delete)):
        os.remove(file)

print('Deleted all files with the specified formats.')
