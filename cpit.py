#! /usr/bin/python3.8

import shutil
import os

# Globals

setted_size_of_movies = 750
source_location = '/home/havellate/Downloads'
raw_files_destination = '/home/havellate/Raw Files'
image_files_destination = '/home/havellate/Pictures'
video_files_destination = '/home/havellate/Videos'
doc_files_destination = '/home/havellate/Documents'
raw_file_extensions = ['.zip', '.iso', '.bin', '.json', '.tgz', '.bz2']
image_file_extensions = ['.jpg', '.png', '.gif']
video_file_extensions = ['.mp4', '.mov', '.wmv', '.flv', '.avi', '.vob', '.avchd', '.mkv', '.srt']
doc_files_extensions = ['.pdf', '.odx']

# Images

for extension in image_file_extensions:
    for dirpath, dirname, files in os.walk(source_location):
        for file in files:
            if file.endswith(extension):
                extension_directory_name = file[-3:].upper() + 's'
                directory_location = image_files_destination + '/' + extension_directory_name
                file_location = os.path.join(source_location, file)
                if not os.path.exists(directory_location):
                    os.mkdir(directory_location)
                shutil.move(file_location, image_files_destination)

# Videos

for extension in video_file_extensions:
    for dirpath, dirname, files in os.walk(source_location):
        for file in files:
            if file.endswith(extension):
                file_location = os.path.join(source_location, file)
                if os.path.getsize(file_location) / 1e+6 > setted_size_of_movies:
                    movies_destination = video_files_destination + '/Entertainment'
                    shutil.move(file_location, movies_destination)
                else:
                    shutil.move(file_location, video_files_destination)

# Documents

for extension in doc_files_extensions:
    for dirpath, dirname, files in os.walk(source_location):
        for file in files:
            if file.endswith(extension):
                extension_directory_name = file[-3:].upper() + 's'
                directory_location = doc_files_destination + '/' + extension_directory_name
                file_location = os.path.join(source_location, file)
                if not os.path.exists(directory_location):
                    os.mkdir(directory_location)
                shutil.move(file_location, directory_location)

# Others

for extension in raw_file_extensions:
    for dirpath, dirnames, files in os.walk(source_location):
        for file in files:
            if file.endswith(extension):
                extension_directory_name = file[-3:].upper() + 's'
                directory_location = raw_files_destination + '/' + extension_directory_name
                file_location = os.path.join(source_location, file)
                if not os.path.exists(directory_location):
                    os.mkdir(directory_location)
                shutil.move(file_location, directory_location)
