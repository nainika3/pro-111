from distutils import extension
import os
import shutil
from unicodedata import name
from_dir = "C:/Users/user/Downloads"
to_dir = "C:/Users/user/Documents"

list_of_files=os.listdir(from_dir)
print(list_of_files)

for file_name in list_of_files:
 name,extension = os.path.splitext(file_name)
 print(name)
 print(extension)