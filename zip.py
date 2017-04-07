import os, zipfile

directory = '/path/of/the/zip/file'
ext = ".zip"

os.chdir(directory)

for item in os.listdir(directory):
    if item.endswith(ext):
        file_name = os.path.abspath(item)
        zip_ref = zipfile.ZipFile(file_name)
        zip_ref.extractall(directory)
        zip_ref.close()
        os.remove(file_name) 	
