import os
import sys
import time


inputs = sys.argv
source = inputs[1]
destination = inputs[2]

for root, dirs, files in os.walk(source):
    for file in files:
        if "." in file and file.split('.')[-1].lower() in ("jpg", "jpeg", "png"):
            file_path = os.path.join(root, file)

            year = time.ctime(os.path.getmtime(file_path)).split()[-1]

            if not os.path.exists(os.path.join(destination, year, 'photos')):
                os.makedirs(os.path.join(destination, year, 'photos'))

            with open(file_path, 'rb') as src_file:
                 binary_data = src_file.read()
            with open(os.path.join(destination, year, 'photos', file), 'wb') as dst_file:
                 dst_file.write(binary_data)
        elif "." in file and file.split('.')[-1].lower() in ("mp4", "avi", "3gp", "mpeg", "mkv", "wmv", "mov"):
            file_path = os.path.join(root, file)
            year = time.ctime(os.path.getmtime(file_path)).split()[-1]
            if not os.path.exists(os.path.join(destination, year, 'videos')):
                os.makedirs(os.path.join(destination, year, 'videos'))

            with open(file_path, 'rb') as src_file:
                binary_data = src_file.read()
            with open(os.path.join(destination, year, 'videos', file), 'wb') as dst_file:
                dst_file.write(binary_data)
